from projects.phase0_1.Resource_Monitor.resource_monitor import resource_monitor
import ollama


def ai_call(message):
    response = ollama.chat(
        model="llama3.1", messages=[{"role": "user", "content": message}]
    )
    return response.message.content


if __name__ == "__main__":
    while True:
        try:
            user_input = input("You: ")
            if user_input in ["q", "quit", "exit"]:
                print("Quitting..")
                break
            else:
                with resource_monitor("AI inference"):
                    print(f"AI: {ai_call(user_input)}")
        except KeyboardInterrupt:
            print("\nFile interrupted.")
            break
