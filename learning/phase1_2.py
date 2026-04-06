list = ['q', 'quit', 'exit']
toolsList = ["open_file", "run_command", "search_web"]
isRunning = True
while isRunning:
    print("")
    userInput = input("Enter command (type 'quit' to exit): ")
    if userInput.lower() == "tools":
        for tool in toolsList:
            print(tool)
    elif userInput in list:
        print("Agent shutting down...")   
        isRunning = False
    else:
        print(f"You said {userInput.upper()}")