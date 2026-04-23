import ollama
from projects.phase0_1.Resilient_AI.memory.memory_manager import MemoryManager
from projects.phase0_1.Resource_Monitor.resource_monitor import resource_monitor


class ChatAgent:
    def __init__(self):
        self.memory = MemoryManager()
        self.isRunning = True
        self.memory.load_history()

    def run(self):
        try:
            while self.isRunning:
                user_input = input("\nYou: ")

                if user_input in ["q", "quit", "exit"]:
                    self.isRunning = False

                elif user_input in ["save", "s"]:
                    self.memory.save_history()

                elif user_input in ["load", "l"]:
                    self.memory.load_history()

                elif user_input == "clear":
                    self.memory.clear_history()

                else:
                    self.memory.add_messages("user", user_input)

                    with resource_monitor("AI inference"):
                        response = ollama.chat(
                            model="llama3.1", messages=self.memory.state["history"]
                        )

                    ai_response = response.message.content
                    self.memory.add_messages("assistant", ai_response)
                    self.memory.increment_interactions()
                    print(ai_response)
        except KeyboardInterrupt:
            print("\nFile interrupted.")
            self.memory.save_history()
            self.isRunning = False


if __name__ == "__main__":
    agent = ChatAgent()
    agent.run()
