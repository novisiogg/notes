import os
import json

class ConfigManager():
    def __init__(self):
        self.default_config = {
            "name": "novisiogg",
            "audio": {
                "language": "english",
                "text_to_speech": "disabled"
            },
            "model": "chatgpt4",
            "auto_save": True
        }
        self.config = self.default_config.copy()
        self.commands = {
            "show": {
                "description": "Shows the config applied to the agent",
                "syntax": "show"
            },
            
            "set": {
                "description": "Set a key from the config to a given value",
                "syntax": "set [key.option] <value>"
            },
            
            "save": {
                "description": "Saves the config to a file",
                "syntax": "save <filename>"
            },
            
            "load": {
                "description": "Loads the config from a file",
                "syntax": "load <filename>"
            },
            
            "reset": {
                "description": "Resets the config to its default values",
                "syntax": "reset"
            },
        }
        self.is_running = True
        
    # shows the current config applied
    
    def show_config(self):
        print(self.config)
    
    # changes keys accoring to the user
    
    def set_key(self, key: str, value):
        try:
            if "." in key:
                # set audio.language french
                parts = key.split(".") # ['audio', 'language']
                if self.config[parts[0]][parts[1]] == value:
                    print(f"Agent: {self.config[parts[0]][parts[1]]} is already set to {value}")
                else:    
                    self.config[parts[0]][parts[1]] = value
                    print(f"Agent: Successfully set {key} to {value}")
            else:
                if self.config.get(key) == value:
                    print(f"Agent: {key} is already set to {value}")
                else:
                    self.config[key] = value
                    print(f"Agent: Successfully set {key} to {value}")
        except:
            print(f"Agent: There was an error changing {key} to {value}.")

    # saves the config to a given path | save <path>
    
    def save_config(self, file):
        if os.path.exists(file):
            print("Agent: File already exists, can't overwrite.")
        else:
            with open(file, "w") as f:
                json.dump(self.config, f)
                print(f"Agent: Successfully saved config to [{file}].")

    # loads a config file
    
    def load_config(self, file):
        if os.path.exists(file):
            with open(file, "r") as f:
                self.config = json.load(f)
                print(f"Agent: Successfully loaded config file [{file}].")

    # resets the config file to default settings
    
    def reset_config(self):
        if self.config == self.default_config:
            print("Agent: Settings are already set to default.")
        else:
            self.config = self.default_config.copy()
            print("Agent: Successfully reset config to default.")
            print("")
            print(self.config)
            
    # shows help for the commands
    def help(self, command_name = None):
        if command_name is None:
            print("")
            print("Agent: Avalaible commands:")
            for cmd, info in self.commands.items():
                print(f"{cmd} - {info['description']}")
            print("")
        else:
            info = self.commands.get(command_name)
            if info:
                print("")
                print(f"Command: {command_name}")
                print(f"Description: {info['description']}")
                print(f"Syntax: {info['syntax']}")
                print("")
            else:
                print(f"Agent: Unknown command '{command_name}'")
    
    def run(self):
        while self.is_running:
            try:
                user_input = input("Listening: ")
                if user_input in ["q", "quit", "exit"]:
                    self.is_running = False
                
                elif user_input.startswith("show"):
                    self.show_config()
                elif user_input.startswith("set "):                    # set name novisiogg 
                        items = user_input[4:]
                        space_pos = items.find(" ")
                        key = items[:space_pos]
                        value = items[space_pos + 1:]
                        if space_pos == -1:
                            self.help("set")
                        else:
                            self.set_key(key, value)
                elif user_input.startswith("save "):
                    file = user_input[5:]
                    self.save_config(file)
                elif user_input.startswith("load "):
                    file = user_input[5:]
                    self.load_config(file)
                elif user_input.startswith("reset"):
                    self.reset_config()
                    
                elif user_input == "help":
                    self.help()
                elif user_input.startswith("help "):
                    self.help(user_input[5:])
                    
                else:
                    print(f"Agent: Unknown command '{user_input}'")
            except KeyboardInterrupt:
                print("Agent: There was an error.")
if __name__ == "__main__":
    config = ConfigManager()
    config.run()