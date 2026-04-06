name = input("enter your name: ")
mode = input("choose voice or chat - v/c: ")
choices = ["v", "c", "voice", "chat"]
timestamp = "just now"
isVoice = False

if mode.lower() in choices:
    if mode.lower() in ["v", "voice"]:
        print("Voice enabled.")
        isVoicesVoice = True
    elif mode.lower() in ["c", "chat"]:
        print("Voice disabled.")
    else:
        print("please type a valid mode.")

config = {
    "name": name,
    "mode": mode,
    "timestamp": timestamp,
    "voice": isVoice,
}

print(f"Agent started for {config['name']}, mode: {config['mode']}, timestamp: {config['timestamp']}, voice active: {config['voice']}")