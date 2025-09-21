from core import Core

if __name__ == "__main__":
    core = Core()
    while True:
        user_request = input("\nWhat do you want me to do? (type 'quit' to exit)\n> ")
        if user_request.lower() in ["quit", "exit"]:
            break
        core.execute_user_request(user_request)
