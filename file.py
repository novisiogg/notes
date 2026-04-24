from pathlib import Path

file_path = Path("C:/Users/vwu/Desktop/notes/docs") / "TAKEAWAYS.md"


class FileManager:
    def __init__(self):
        self.filename = file_path
        self.is_running = True
        print("Usage: add <phase_num> <phase_title>")

    def load(self):
        if self.filename.exists():
            return self.filename.read_text(encoding="utf-8")
        self.filename.touch()
        print("file created.")
        return ""

    def save(self, content):
        self.filename.write_text(content, encoding="utf-8")

    def build_phase(self, phase_num, phase_title):
        return f"""## Phase {phase_num} — [{phase_title}]

## Core Concepts & Patterns
- [Add concepts here]

## Code Patterns & Snippets
```python
# Your snippets here
```

## Bugs/Issues Fixed
1. [Fix description]

## Exercises/Projects Done
- [Work done]
"""

    def add_phase(self, phase_num, phase_title):
        content = self.load()
        new_phase = self.build_phase(phase_num, phase_title)

        updated = content + f"""\n---\n""" + new_phase if content else new_phase
        self.save(updated)

        print(f"Added Phase {phase_num} — {phase_title}")

    def run(self):
        try:
            while self.is_running:
                user_input = input("> ")

                if user_input in ["q", "quit", "exit"]:
                    self.is_running = False
                    print("have a nice day!")

                elif user_input.startswith("add "):
                    args = user_input[4:].strip()
                    parts = args.split(" ", 1)

                    if len(parts) < 2:
                        print("Usage: add <phase_num> <phase_title>")
                        continue

                    phase_num, phase_title = parts
                    self.add_phase(phase_num, phase_title)

                else:
                    print("Invalid command.")

        except KeyboardInterrupt:
            print("\ninterrupted")


if __name__ == "__main__":
    file = FileManager()
    file.run()
