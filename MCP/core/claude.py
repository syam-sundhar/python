import os
import json
from types import SimpleNamespace
from anthropic import Anthropic
from anthropic.types import Message
import httpx


class _OpenRouterMessage:
    """A minimal wrapper that mimics anthropic.types.Message for OpenRouter responses."""

    def __init__(self, text: str, stop_reason: str = "end_turn"):
        block = SimpleNamespace(type="text", text=text)
        self.content = [block]
        self.stop_reason = stop_reason


class Claude:
    def __init__(self, model: str):
        self.model = model
        api_key = os.getenv("ANTHROPIC_API_KEY", "")

        if api_key.startswith("sk-or-"):
            # OpenRouter only supports the OpenAI-compatible endpoint (/chat/completions)
            # NOT the Anthropic /messages endpoint, so we bypass the Anthropic SDK entirely.
            self._mode = "openrouter"
            self._api_key = api_key
            self._http = httpx.Client(timeout=60.0)
        else:
            self._mode = "anthropic"
            self.client = Anthropic(api_key=api_key)

    # ── Helpers ────────────────────────────────────────────────────────────────

    def _extract_content(self, message):
        """Returns JSON-serializable content from any message type."""
        if isinstance(message, Message):
            # Anthropic native: list of content blocks (already serializable dicts)
            return message.content
        if isinstance(message, _OpenRouterMessage):
            # Our wrapper: store as plain string for OpenAI-compatible history
            return self.text_from_message(message)
        # Already a string or serializable value
        return message

    def add_user_message(self, messages: list, message):
        messages.append({
            "role": "user",
            "content": self._extract_content(message),
        })

    def add_assistant_message(self, messages: list, message):
        messages.append({
            "role": "assistant",
            "content": self._extract_content(message),
        })

    def text_from_message(self, message) -> str:
        return "\n".join(
            [block.text for block in message.content if block.type == "text"]
        )

    # ── Main Chat ──────────────────────────────────────────────────────────────

    def chat(
        self,
        messages,
        system=None,
        temperature=1.0,
        stop_sequences=[],
        tools=None,
        thinking=False,
        thinking_budget=1024,
    ):
        if self._mode == "openrouter":
            return self._chat_openrouter(messages, system, temperature, tools)
        else:
            return self._chat_anthropic(
                messages, system, temperature, stop_sequences, tools, thinking, thinking_budget
            )

    # ── OpenRouter (OpenAI chat/completions format) ────────────────────────────

    def _convert_messages_for_openai(self, messages: list, system: str | None) -> list:
        """Convert Anthropic-style messages to OpenAI format."""
        openai_messages = []
        if system:
            openai_messages.append({"role": "system", "content": system})
        for msg in messages:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            # Handle list content (tool results, etc.) — flatten to string
            if isinstance(content, list):
                text_parts = []
                for block in content:
                    if isinstance(block, dict):
                        if block.get("type") == "text":
                            text_parts.append(block.get("text", ""))
                        elif block.get("type") == "tool_result":
                            text_parts.append(str(block.get("content", "")))
                    elif hasattr(block, "text"):
                        text_parts.append(block.text)
                content = "\n".join(text_parts)
            openai_messages.append({"role": role, "content": content})
        return openai_messages

    def _chat_openrouter(self, messages, system, temperature, tools) -> _OpenRouterMessage:
        openai_messages = self._convert_messages_for_openai(messages, system)

        payload: dict = {
            "model": self.model,
            "messages": openai_messages,
            "temperature": min(temperature, 2.0),
            "max_tokens": 8000,
        }

        # Convert Anthropic-style tools to OpenAI format
        if tools:
            payload["tools"] = [
                {
                    "type": "function",
                    "function": {
                        "name": t["name"],
                        "description": t.get("description", ""),
                        "parameters": t.get("input_schema", {}),
                    },
                }
                for t in tools
            ]

        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
            "X-Title": "MCP Chat",
        }

        response = self._http.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            content=json.dumps(payload),
        )

        if response.status_code != 200:
            raise RuntimeError(
                f"OpenRouter error {response.status_code}: {response.text[:500]}"
            )

        data = response.json()
        choice = data["choices"][0]
        finish_reason = choice.get("finish_reason", "stop")
        stop_reason = "end_turn" if finish_reason in ("stop", "length") else finish_reason

        text = choice["message"].get("content") or ""
        return _OpenRouterMessage(text=text, stop_reason=stop_reason)

    # ── Anthropic (native) ─────────────────────────────────────────────────────

    def _chat_anthropic(
        self, messages, system, temperature, stop_sequences, tools, thinking, thinking_budget
    ) -> Message:
        params = {
            "model": self.model,
            "max_tokens": 8000,
            "messages": messages,
            "temperature": temperature,
            "stop_sequences": stop_sequences,
        }
        if thinking:
            params["thinking"] = {"type": "enabled", "budget_tokens": thinking_budget}
        if tools:
            params["tools"] = tools
        if system:
            params["system"] = system

        return self.client.messages.create(**params)
