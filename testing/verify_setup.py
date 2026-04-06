import os
from openai import OpenAI
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)
while True:
    userInput = input("Listening: ")
    if userInput.lower() in ["quit", "q", "exit", "stop"]:
        break
    stream = client.responses.create(
        model="llama-3.3-70b-versatile",
        instructions="ONLY answer AI-related questions",
        input=f"{userInput}",
        stream=True,
    )
    print()
    print("AI: ", end="", flush=True)
    for word in stream:
        if word.type == "response.output_text.delta":
            print(word.delta, end="", flush=True)
    print()