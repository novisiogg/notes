import requests
from requests.exceptions import RequestException
from phase2_3 import ConfigManager
import sys
sys.path.append(".")

class ChatAgent(ConfigManager):
    def __init__(self):
        super.__init__()
        self.history = []
    
    def get_reply(self, user_message):
        self.history.append("user", user_message)
        payload = {"model": self.config.get("model"), "messages": self.history}
        

