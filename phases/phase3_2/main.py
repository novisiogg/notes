import memory
from memory import MemoryManager
import sys
import ollama
from ollama import chat, ChatResponse

sys.path.append("")


class ChatAgent(MemoryManager):
    def __init__(self):
        super().__init__()
        self.is_running = True
        self.load()
        interactions = self.state["metadata"]["total_interactions"]
        print(f"Interactions: {interactions}")

    def run(self):
        try:
            if self.state["metadata"]["total_interactions"] == 1:
                print("Initial setup complete.")
                print("Memory file created.")

            elif self.state["metadata"]["total_interactions"] > 1:
                print("Resuming previous session...")

            while self.is_running:
                user_input = input("> ")
                if user_input in ["q", "quit", "exit"]:
                    self.is_running = False

                elif user_input == "load":
                    self.load()

                elif user_input == "save":
                    self.save()

                elif user_input == "clear":
                    print(self.clear())

                else:
                    self.add_chat_entry("user", user_input)
                    print(f"\nAI is thinking...")
                    response: ChatResponse = chat(
                        model="llama3.1", messages=self.state["history"]
                    )
                    bot_txt = response.message.content
                    print(f"\n{response.model}: {bot_txt}")
                    self.add_chat_entry("assistant", bot_txt)
                    self.update_interactions()
                    self.save()

        except KeyboardInterrupt:
            print("System crashed, saving state..")
            print(self.save())


if __name__ == "__main__":
    agent = ChatAgent()
    agent.run()
