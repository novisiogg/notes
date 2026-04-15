import json
import os


class MemoryManager:
    def __init__(self, filename="storage.json"):
        self.state = {} # Edit this so it loads with the parameter by default

    def save(self):
        try:
            with open("storage.json", "w") as f:
                json.dump(self.state, f, indent=4)
                return f"Successfully saved state to {f.name}."

        except FileNotFoundError:
            print("File does not exist or corrupted.")

    def load(self):
        if os.path.exists("storage.json"):
            with open("storage.json", "r") as f:
                data = json.load(f)
                self.state = data
                print(f"Successfully loaded history from [{f.name}].")
                self.save()
        else:
            print(f"File not found.")
            print(f"Creating a new one..")
            with open("storage.json", "w") as f:
                self.state = {
                    "metadata": {"total_interactions": 0},
                    "history": [
                        {
                            "role": "system",
                            "content": "You are a witty, helpful AI assistant named Jarvis.",
                        }
                    ],
                }
                json.dump(self.state, f)
                self.save()

    def clear(self):
        if os.path.exists("storage.json"):
            self.state["history"] = []
            self.save()
            return f"Successfully cleared the history."
        else:
            return f"File not found."

    def update_interactions(self):
        self.state["metadata"]["total_interactions"] += 1
        self.save()

    def add_chat_entry(self, role, content):
        messages = {"role": role, "content": content}
        self.state["history"].append(messages)
        self.save()
