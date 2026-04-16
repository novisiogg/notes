import sys
from tools import WeatherManager

sys.path.append("")


class ChatAgent(WeatherManager):
    def __init__(self):
        super().__init__()
        self.is_running = True

    def run(self):
        try:
            self.load_file()
            while self.is_running:
                user_input = input("> ")

                if user_input in ["q", "quit"]:
                    self.is_running = False
                    print(self.save_file())

                else:
                    self.get_response(user_input)
        except KeyboardInterrupt:
            print("Terminal was interrupted..")
            print(self.save_file())


if __name__ == "__main__":
    agent = ChatAgent()
    agent.run()
