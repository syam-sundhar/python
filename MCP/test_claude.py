import os, sys
sys.path.insert(0, ".")
from dotenv import load_dotenv
load_dotenv()

from core.claude import Claude

model = os.getenv("CLAUDE_MODEL")
print(f"Testing multi-turn with model: {model}\n")

claude = Claude(model=model)
messages = []

# Turn 1
claude.add_user_message(messages, "My name is Syam. Remember it.")
resp1 = claude.chat(messages=messages)
claude.add_assistant_message(messages, resp1)
print("Turn 1:", claude.text_from_message(resp1))

# Turn 2
claude.add_user_message(messages, "What is my name?")
resp2 = claude.chat(messages=messages)
claude.add_assistant_message(messages, resp2)
print("Turn 2:", claude.text_from_message(resp2))

print("\nMulti-turn OK!")
