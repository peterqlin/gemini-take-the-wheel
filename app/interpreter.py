import pyautogui
import json

def open_app(app_name: str, **kwargs):
    print(f"Opening {app_name}...")
    pyautogui.press("win")
    pyautogui.write(app_name, interval=0.25)
    pyautogui.press("enter")

functions = {
    "open_app": open_app
}

class Interpreter:
    def __init__(self):
        self.context = ""

    def process_function(self, fn: dict) -> bool:
        try:
            name, args = fn["name"], fn["args"]
            print(f"[DEBUG] Gemini wants to call {name} with args {args}")
            functions[name](**args)
            self.context = args["context"]
            print("[DEBUG] Command executed successfully")
            return args["continue"]
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
