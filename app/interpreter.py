import pyautogui
import json

def open_app(app_name: str, **kwargs):
    print(f"Opening {app_name}...")
    pyautogui.press("win")
    pyautogui.write(app_name, interval=0.25)
    pyautogui.press("enter")

def write_text(text: str, enter: bool, **kwargs) -> None:
    print(f"Writing {text}{enter and " and hitting enter"}...")
    pyautogui.write(text, interval=0.25)
    if enter:
        pyautogui.press("enter")

functions = {
    "open_app": open_app,
    "write_text": write_text,
}

class Interpreter:
    def __init__(self):
        self.history = ""
    
    def append_history(self, history):
        self.history += history

    def process_function(self, fn: dict) -> bool:
        try:
            name, args = fn["name"], fn["args"]
            # print(f"[DEBUG] Gemini wants to call {name} with args {args}")
            print("➡️\t", end="")
            functions[name](**args)
            self.history += f"{args["next_steps"]}"
            print(f"Current history: {self.history}")
            print("[DEBUG] Command executed successfully")
            return args["continue"]
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
