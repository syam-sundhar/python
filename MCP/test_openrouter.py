import httpx
import json
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("ANTHROPIC_API_KEY")

models = [
    "anthropic/claude-3.5-haiku",
    "anthropic/claude-3-haiku",
    "meta-llama/llama-3.1-8b-instruct:free",
    "google/gemini-2.0-flash-exp:free",
    "mistralai/mistral-7b-instruct:free",
    "openai/gpt-4o-mini",
]

headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "MCP Chat",
}

print("Testing OpenRouter API key and models...\n")
for model in models:
    try:
        r = httpx.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            content=json.dumps({
                "model": model,
                "messages": [{"role": "user", "content": "Say hi"}],
                "max_tokens": 10,
            }),
            timeout=20,
        )
        if r.status_code == 200:
            reply = r.json()["choices"][0]["message"]["content"]
            print(f"WORKS: {model}")
            print(f"       Reply: {reply}")
            break
        else:
            err = r.json().get("error", {}).get("message", r.text[:120])
            print(f"FAIL  ({r.status_code}): {model}")
            print(f"       {err}")
    except Exception as e:
        print(f"ERROR: {model} -> {e}")
