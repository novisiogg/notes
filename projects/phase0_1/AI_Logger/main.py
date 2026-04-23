from projects.phase0_1.AI_Logger.decorator import ai_logger
import ollama


@ai_logger
def ai_call(message):
    response = ollama.chat(
        model="llama3.1", messages=[{"role": "user", "content": message}]
    )
    bot_txt = response.message.content
    return f"AI: {bot_txt}"


if __name__ == "__main__":
    while True:
        try:
            user_input = input("You: ")
            if user_input in ["q", "quit", "exit"]:
                break
            else:
                print(ai_call(user_input))
        except KeyboardInterrupt:
            print("\nFile interrupted.")
            break
