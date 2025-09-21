from interpreter import Interpreter
from llm import LLM

class Core:
    def __init__(self):
        self.interpreter = Interpreter()
        self.llm = LLM()
        self.max_fn_calls = 3

    def execute_user_request(self, user_request: str):
        try:
            fns = self.llm.get_function_calls(user_request)
            self.interpreter.process_function(fns)
        except Exception as e:
            print(f"Error executing request: {e}")
