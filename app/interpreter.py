import pyautogui
import time
import json

def open_app(app_name: str):
    print(f"Opening {app_name}...")
    pyautogui.press("win")
    pyautogui.write(app_name, interval=0.25)
    pyautogui.press("enter")

functions = {
    "open_app": open_app
}

class Interpreter:
    def process_function(self, fn: dict) -> bool:
        try:
            print(f"[DEBUG] Gemini wants to call {fn.name} with args {fn.args}")
            functions[fn.name](**fn.args)
            print("[DEBUG] Command executed successfully")
            return True
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
