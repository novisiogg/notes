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
            
    def run(self):
        list = ["q", "quit", "exit",]
        tools = ["open_file", "run_command", "search_web"]
        while self.isRunning:
            try:    
                userInput = input(f"[{self.mode}] Enter a command: ")
                if userInput.lower() == "tools":
                    for tool in tools:
                        print(tool)
            
                elif userInput.lower() == "toggle":
                    print(self.toggleMode())
            
                elif userInput.lower() in list:
                    print(f"Agent quitting...")
                    self.isRunning = False
                else:
                    self.processCommand(userInput)  
            except KeyboardInterrupt:
                print(f"Agent interrupted. Goodbye.")
                self.isRunning = False
                
if __name__ == "__main__":
    agent = Agent("novisiogg", "voice")
    agent.run()