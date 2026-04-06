"""
Phase 2.1 — File I/O
Exercise: Add save_state() and load_state() to the Agent class.
Add "save" and "load" commands to the main command processor.
"""


class Agent():
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.isRunning = True

    def toggleMode(self):
        if self.mode == "voice":
            self.mode = "chat"
        elif self.mode == "chat":
            self.mode = "voice"
        return f"Switched to {self.mode}"

    def divide(self, args: str):
        try:
            a, b = map(int, args.split())
            print(f"Result: {a/b}")
        except ZeroDivisionError:
            print("Can't divide by 0")
        except ValueError:
            print("Invalid numbers.")

    def processCommand(self, command: str):
        if command.startswith("open "):
            appName = command[5:]
            print(f"Launching {appName}")
        elif command.startswith("run "):
            scriptName = command[4:]
            print(f"Executing {scriptName}")
        elif command.startswith("divide "):
            self.divide(command[7:])
        else:
            print(f"Unkown command '{command}'")
    def saveState(self):
        with open("agent_state.txt", "w") as f:
            f.write(f"{self.name} | {self.mode}")
        print(f"State saved")
    def loadState(self):
        with open("agent_state.txt", "r") as f:
            data = f.read()
            parts = data.split(" | ")
            self.name = parts[0]
            self.mode = parts[1]
        print(f"State loaded. Name: {self.name} Mode: {self.mode}")
    def run(self):
        quit_commands = ["q", "quit", "exit"]
        tools = ["open_file", "run_command", "search_web"]
        while self.isRunning:
            try:
                userInput = input(f"[{self.mode}] Enter a command: ")
                if userInput.lower() == "save":
                    self.saveState()
                elif userInput.lower() == "load":
                    self.loadState()
                elif userInput.lower() == "tools":
                    for tool in tools:
                        print(tool)
                elif userInput.lower() == "toggle":
                    print(self.toggleMode())
                elif userInput.lower() in quit_commands:
                    print(f"Agent shutting down...")
                    self.isRunning = False
                else:
                    self.processCommand(userInput)
            except KeyboardInterrupt:
                print(f"Agent interrupted. Goodbye.")
                self.isRunning = False


if __name__ == "__main__":
    agent = Agent("novisiogg", "chat")
    agent.run()
