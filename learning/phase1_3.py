def toggle_mode(mode):
    if mode == "chat":
        return "voice"
    elif mode == "voice":
        return "chat"
    else:
        return "unkown"

def format_message(username, text):
        return f"[{username}]: {text}"

def process_command(command: str):
    if command.startswith("open "):
        app_name = command[5:]
        return f"Launching {app_name}"
    elif command.startswith("run "):
        script_name = command[4:]
        return f"Executing {script_name}"
    else:
        return f"Unkown command {command}"

def main():
    result = toggle_mode("chat")
    print(f"Toggled mode: {result}")

    result = format_message("novisio", "hey")
    print(f"Formatted: {result}")

    result = process_command("open google maps")
    print(f"Command: {result}")
if __name__ == "__main__":
    main()