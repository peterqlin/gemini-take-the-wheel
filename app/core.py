from interpreter import Interpreter
from llm import LLM

class Core:
    def __init__(self):
        self.interpreter = Interpreter()
        self.llm = LLM()
        self.max_fn_calls = 3

    def execute_user_request(self, user_request: str):
        try:
            fn = self.llm.get_function_call(user_request)
            fn_call_count = 0
            self.interpreter.append_history(f"Original objective: {user_request}. ")
            while fn_call_count < self.max_fn_calls and self.interpreter.process_function(fn):
                fn = self.llm.get_function_call(self.interpreter.history)
                fn_call_count += 1
        except Exception as e:
            print(f"Error executing request: {e}")
