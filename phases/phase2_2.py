import os
import subprocess

class WorkspaceManager:
    def __init__(self, name):
        self.name = name
        self.isRunning = True
        self.commands = {
            "create": {
                "description": "Creates a new directory.",
                "aliases": ['new', 'make'],
                "syntax": "create <path>",
            },
            
            "go": {
                "description": "Changes to a new directory.",
                "aliases": ['change to', 'cd'],
                "syntax": "go <path>",
            },
            
            "save": {
                "description": "Creates a file and saves content to it.",
                "aliases": ['touch'],
                "syntax": "store 'filename'[content]",
            },
            
            "read": {
                "description": "Reads a file.",
                "aliases": [''],
                "syntax": "read 'filename'",
            },
            "execute": {
                "description": "Executes a command.",
                "aliases": ['exec'],
                "syntax": "execute '<cmd>'",
            },
            
            "list": {
                "description": "Lists the iems of a working directory.",
                "aliases": ['ls'],
                "syntax": "list",
            },
            
            "where": {
                "description": "Shows the path of the current working directory.",
                "aliases": ['pwd', 'whereami'],
                "syntax": "where",
            }, 
        }
        
        
    def create(self, filepath: str):
        if os.path.isdir(filepath):
            print(f"Agent: Directory already exists")
        else:
            os.makedirs(filepath)
            print(f"Agent: Successfully created directory at {filepath}")
    
    def store(self, filename: str, content):
        with open(filename, "w") as f:
            f.write(content)
        print(f"Agent: Successfully created file {filename}")
    
    def recall(self, filename):
        try:
            with open(filename, "r") as f:
                text = f.read()
            print(f"Agent: Successfully read {filename}, Data: {text}")

        except FileNotFoundError:
            print(f"Agent: File not found. {filename}")

    def execute(self, command: str):
        if command.startswith("start "):
            subprocess.Popen(command[6:], shell=True, )
        elif command.startswith("run "):
           result = subprocess.run(command[6:], shell=True, text=True)
           print(result.stdout)
        else:
            print(f"Agent: Unkown command {command}")
    
    def listItems(self):
        items = os.listdir()
        for i, item in enumerate(items):
            print(f"{i}, {item}")
    
    def where(self):
        directory = os.getcwd()
        print(f"Agent: Current working dir: {directory}")

    def go(self, dir):
        try:
            currentDir = os.getcwd()
            targetDir = os.path.abspath(dir)
            if currentDir == targetDir:
                print(f"Agent: Already inside {dir}")
            else:
                os.chdir(dir)
                print(f"Agent: Successfully changed to {dir}")
                
        except FileNotFoundError:
            print("Agent: Directory or the file doesn't exist")
            
    def help(self, commandName = None):
        if commandName is None:
            print("")
            print("Agent: Avalaible commands:")
            for cmd, info in self.commands.items():
                aliases = ", ".join(info["aliases"])
                print(f"{cmd} ({aliases}) - {info['description']}")
        else:
            info = self.commands.get(commandName)
            if info:
                aliases = ','.join(info["aliases"])
                print("")
                print(f"Command: {commandName}")
                print(f"Description: {info['description']}")
                print(f"Aliases: {aliases}")
                print(f"Syntax: {info['syntax']}")
            else:
                print(f"Agent: Unknown command '{commandName}'")

    def run(self):
        exitList = ['q', 'exit', 'quit']
        showList = ['ls', 'list']

        while self.isRunning:
            try:
                print("")
                userInput = input("Enter a command - ('q' to exit): ")
                # checks if the user wants to quit.
                if userInput in exitList:
                    self.isRunning = False
                # ls command
                elif userInput in showList:
                    self.listItems()
                # pwd command      
                elif userInput.startswith("pwd") or userInput.startswith("where") or userInput.startswith("whereami"):
                    self.where()
                    
                # cd command       
                elif userInput.startswith("change to "):
                    self.go(userInput[10:])
                elif userInput.startswith("go to " ):
                    self.go(userInput[6:])
                elif userInput.startswith("cd "):
                    self.go(userInput[3:])
                    
                # create command   
                elif userInput.startswith("new "):
                    self.create(userInput[4:])
                elif userInput.startswith("create "):
                    self.create(userInput[7:])
                elif userInput.startswith("make "):
                    self.create(userInput[5:])
                    
                # read command  
                elif userInput.startswith("read "):
                    self.recall(userInput[5:])
                    
                # store command        
                elif userInput.startswith("save "):
                    afterSave = userInput[5:]
                    firstSpace = afterSave.find(" ")
                    fileName = afterSave[:firstSpace]
                    content = afterSave[firstSpace+1:]
                    if content != "":
                        self.store(fileName, content)
                    else:
                        self.store(fileName, "")
                        
                # execute command        
                elif userInput.startswith("exec "):
                    self.execute(userInput[5:])
                elif userInput.startswith("execute "):
                    self.execute(userInput[8:])
                    
                # help command       
                elif userInput == "help":
                    self.help()
                elif userInput.startswith("help "):
                    self.help(userInput[5:])
                        
                else:
                    print(f"Agent: Unkown command. [{userInput}]")
            except KeyboardInterrupt:
                print("Agent: Erorr.")
                self.isRunning = False
if __name__ == "__main__":
    workspace = WorkspaceManager("novisiogg")
    workspace.run()