from interpreter import Interpreter
from llm import LLM

class Core:
    def __init__(self):
        self.interpreter = Interpreter()
        self.llm = LLM()

    def execute_user_request(self, user_request: str):
        try:
            instructions = self.llm.get_instructions_for_objective(user_request)
            for step in instructions.get("steps", []):
                print(f"[DEBUG] Current step: {step}")
                self.interpreter.process_function(step)
            if instructions.get("done"):
                print(f"\n✅ Done: {instructions['done']}")
        except Exception as e:
            print(f"⚠️ Error executing request: {e}")
