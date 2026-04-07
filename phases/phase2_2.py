import os
import subprocess

class WorkspaceManager:
    def __init__(self, name):
        self.name = name
        
        
    def create(self, filepath: str):
        os.makedirs(filepath, exist_ok= True)
        print(f"Agent: Successfully created dir: {filepath}")
    
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
        if command.startswith("start"):
            subprocess.run(command[5:])