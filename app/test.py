
step_1 = {
    "name": "step_1",
    "description": "Do step 1.",
    "parameters": {
        "type": "object",
        "properties": {
            "instructions": {
                "type": "string",
                "description": "The instructions for step 1.",
            }
        },
        "required": ["instructions"],
    },
}
step_2 = {
    "name": "step_2",
    "description": "Do step 2.",
    "parameters": {
        "type": "object",
        "properties": {
            "instructions": {
                "type": "string",
                "description": "The instructions for step 2.",
            }
        },
        "required": ["instructions"],
    },
}
open_app_decl = {
    "name": "open_app",
    "description": "Searches for and opens an application on the current device via spotlight search.",
    "parameters": {
        "type": "object",
        "properties": {
            "app_name": {
                "type": "string",
                "description": "The name of the app to open.",
            },
        },
        "required": ["app_name"]
    },
}

write_text_decl = {
    "name": "write_text",
    "description": f"Writes text to the currently selected text box and optionally hits enter afterwards.",
    "parameters": {
        "type": "object",
        "properties": {
            "text": {
                "type": "string",
                "description": "The text to write to the selected text box.",
            },
            "enter": {
                "type": "boolean",
                "description": "Whether to hit enter after writing the text.",
            },
        },
        "required": ["text", "enter"],
    },
}

import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

# Configure the client and tools
client = genai.Client(api_key=api_key)
house_tools = [
    types.Tool(function_declarations=[open_app_decl, write_text_decl])
]
config = types.GenerateContentConfig(
    tools=house_tools,
    automatic_function_calling=types.AutomaticFunctionCallingConfig(
        disable=True
    ),
    # Force the model to call 'any' function, instead of chatting.
    tool_config=types.ToolConfig(
        function_calling_config=types.FunctionCallingConfig(mode='ANY')
    ),
)

chat = client.chats.create(model="gemini-2.5-flash", config=config)

start_time = time.time()

response = chat.send_message("Open chrome, then search for today's weather.")

elapsed = time.time() - start_time
print(f"[DEBUG] Gemini API call took {elapsed:.2f} seconds.")

# Print out each of the function calls requested from this single call
print("Example 1: Forced function calling")
for fn in response.function_calls:
    args = ", ".join(f"{key}={val}" for key, val in fn.args.items())
    print(f"{fn.name}({args})")