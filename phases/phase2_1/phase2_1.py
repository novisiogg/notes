class TaskQueue:
    def __init__(self, name):
        self.name = name
        self.queueList = []
        self.processedList = []
        self.isRunning = True
        
    def addTask(self, command: str):
        self.queueList.append(command)
        print(f"Number of tasks pending: {len(self.queueList)}")
        
    def processNext(self):
        if self.queueList:
            firstItem = self.queueList[0]
            if firstItem.startswith("open "):
                appName = firstItem[5:]
                print(f"Agent: Opening [{appName}]")
            elif firstItem.startswith("run "):
                scriptName = firstItem[5:]
                print(f"Agent: Running [{scriptName}]")
            elif firstItem.startswith("ask "):
                question = firstItem[4:]
                print(f"Agent: Sending to LLM: [{question}]")
            else:
                print(f"Agent: Unkown command: [{firstItem}]")
            self.queueList.pop(0)
            self.processedList.append(firstItem)

    def showQueue(self):
        print("Pending tasks:")
        for i, task in enumerate(self.queueList, 1):
            print(f"{i}. {task}")
            
    def showProcessed(self):
        print("Completed tasks:")
        for i, task in enumerate(self.processedList, 1):
            print(f"{i}. {task}")
    
    def saveQueue(self):
        with open("textfile.txt" , "w") as f:
            f.write("--Queue--\n")
            for task in self.queueList:
                f.write(task + "\n")
            f.write("--Processed--\n")
            for task in self.processedList:
                f.write(task + "\n")
    
    def loadQueue(self):
        try:
            with open("textfile.txt", "r") as f:
                text = f.read()
                tasks = text.split("--Processed--")
                queueSection = tasks[0].split('\n')
                processedSection = tasks[1].split('\n')
                self.queueList = queueSection[1:-1]
                self.processedList = processedSection[:-1]
        except FileNotFoundError:
            print("No save queue found.")
            
    def run(self):
        exitList = ['q', 'quit', 'exit']
        while self.isRunning:
            try:
                userInput = input("Enter a command - ('q' or 'quit' to exit): ")
                if userInput in exitList:
                    print(f"[Agent]: Quitting...")
                    self.isRunning = False
                elif userInput == "save":
                    self.saveQueue()
                elif userInput == "load":
                    self.loadQueue()
                elif userInput == "show":
                    self.showQueue()
                elif userInput == "log":
                    self.showProcessed()
                elif userInput.startswith("add "):
                    rest = userInput[4:]
                    self.addTask(rest)
                elif userInput.startswith("next"):
                    self.processNext()
                else:
                    print(f"Unkown command: {userInput}")
            except KeyboardInterrupt:
                print("Error.")
                self.isRunning = False

if __name__ == "__main__":
    task = TaskQueue("novisiogg")
    task.run()
                
                
    
  