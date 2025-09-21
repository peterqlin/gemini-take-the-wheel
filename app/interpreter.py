import pyautogui
import json

def open_app(app_name: str) -> None:
    print(f"Opening {app_name}...")
    pyautogui.press("win")
    pyautogui.write(app_name, interval=0.25)
    pyautogui.press("enter")

def write_text(text: str, enter: bool) -> None:
    print(f"Writing {text}{enter and " and hitting enter"}...")
    pyautogui.write(text, interval=0.25)
    if enter:
        pyautogui.press("enter")

functions = {
    "open_app": open_app,
    "write_text": write_text,
}

class Interpreter:
    def process_function(self, fns: list) -> None:
        try:
            for fn in fns:
                print(f"[DEBUG] Running {fn.name} with args {fn.args}")
                functions[fn.name](**fn.args)
            print("[DEBUG] Command executed successfully")
        except Exception as e:
            print(f"❌ Error: {e}")
