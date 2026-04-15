import requests
from requests.exceptions import RequestException
from phases.phase2_3.phase2_3 import ConfigManager
import sys
sys.path.append(".")

class ChatAgent(ConfigManager):
    def __init__(self):
        super().__init__()
        self.is_running = True
        self.history = []

        print("Agent: Welcome! Type a message, 'clear' to reset history,")
        print("'status' to see config, or 'quit' to exit.")


    def get_reply(self, user_message):
        self.history.append({"role": "user", "content": user_message})
        payload = { # what gets sent to the server. 
            "model": self.config.get("model"),
            "messages": self.history
        }
        try:
            response = requests.post( # sendin payload to the server
                self.config.get("api_endpoint", "http://localhost:5000/api/chat"),
                json=payload,
                timeout=3
            )
            reply = response.json()["reply"]
            
        except RequestException:
            reply = "LLM server offline."

        self.history.append({
            "role": "assistant", "content": reply
        })
        return reply 
    
    def show_status(self):
        print(f"Model: {self.config.get('model')}")
        print(f"API endpoint: {self.config.get('api_endpoint', 'http://localhost:5000/api/chat')}")

    def clear_history(self):
        self.history = []
        print(f"Agent: Successfully cleared history")

    def run(self):
        
        while self.is_running:
            user_input = input("> ")
            
            if user_input in ['q', 'quit', 'exit']:
                self.is_running = False
            
            elif user_input == "status" or user_input == "show status":
                self.show_status()

            elif user_input == "clear" or user_input == "clear history":
                self.clear_history()

            else:
                print(f"You: {user_input}")
                reply = self.get_reply(user_input)
                print(f"Agent: {reply}")
if __name__ == "__main__":
    agent = ChatAgent()
    agent.run()
            
            
