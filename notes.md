# Phase 1.1 — Variables, Types, Input/Output

**Variables** are named containers for data.
**Types** matter — the same operations don't work on all types.

| Type | Example | Use in agent |
|---|---|---|
| `str` | `"hello"` | All text: prompts, responses, commands |
| `int` | `42` | Counting tokens, retries, loop counters |
| `float` | `0.7` | Temperature (controls AI creativity) |
| `bool` | `True` / `False` | Mode toggle |
| `list` | `["open", "calc"]` | Command parts |
| `dict` | `{"name": "Alice"}` | Config, API payloads |

**Key bugs fixed:**
1. `config[name]` vs `config["name"]` — variable vs string key
2. `mode == "v" or "voice"` — `or` doesn't chain like that (non-empty strings are truthy)
3. `config` built before `isVoice` was updated — code execution order matters
4. `{config["name"], mode: ...}` in f-string — comma creates tuple, colon is format specifier

---

# Phase 1.2 — Control Flow

**While loop** — keeps the agent running until quit
**For loop** — iterates through lists (tools, commands)
**Break** — exits a loop early
**`input()` inside while** — the agent's main loop pattern

**Key pattern:**
```python
while self.isRunning:
    user_input = input("Command: ")
    if user_input == "quit":
        self.isRunning = False
```

---

# Phase 1.3 — Functions & Modules

**Why:** Each agent action (open app, LLM request, voice convert) is its own function.

**Key concepts:**
- `def name(params):` — defines a function
- `return` — sends result back to caller
- `if __name__ == "__main__":` — "only run this when file is executed directly, not when imported"
- `.startswith()` — string method for checking command prefixes
- `string[5:]` — slicing: everything from position 5 to the end

**Functions built:**
- `toggle_mode(mode)` — swap chat ↔ voice
- `format_message(username, text)` — format as `"[username]: text"`
- `process_command(cmd)` — parse "open ", "run ", unknown

**Key fix:** `process_command` hardcodes outputs → fix with slicing: `command[5:]` extracts what the user typed after "open "

---

# Phase 1.4 — Classes & OOP

**WHY:** Classes bundle data (`self.name`, `self.mode`, `self.isRunning`) with the methods that use them. No passing variables around manually anymore.

**Key concepts:**
- `class` — blueprint for objects
- `__init__` — constructor, runs when you create an object
- `self` — the object referring to itself. `self.mode` = this object's mode, not some other object's
- Methods — functions that belong to the object
- Instantiation — `agent = Agent("name", "chat")`

**Agent class methods:**
- `__init__(self, name, mode)` — set up `self.name`, `self.mode`, `self.isRunning = True`
- `toggleMode(self)` — flip `self.mode` between "chat" and "voice", no parameter needed (it already knows `self.mode`)
- `processCommand(self, command)` — parse and handle "open ", "run " commands
- `run(self)` — main loop: ask input, handle quit/toggle/tools, delegate to processCommand

**Key bugs fixed:**
1. `processCommand` nested functions should be at class level, not inside other methods
2. `return` inside loop exits the method — use `print` for feedback in a loop
3. No `else` branch in `run()` → unknown input does nothing
4. `toggleMode` returns string but nobody prints it

---

# Phase 1.5 — Error Handling

**WHY:** Agent shouldn't crash when user divides by zero, enters bad input, or presses Ctrl+C.

**Key concepts:**
- `try/except` — attempts risky code, catches specific errors
- `try/except ValueError` — catches `int("abc")` failures
- `try/except ZeroDivisionError` — catches division by zero
- `try/except KeyboardInterrupt` — catches Ctrl+C (no crash stack trace)

**Methods added:**
- `divide(self, args)` — parses `"10 2"`, divides, handles edge cases
- `try` block around `input()` in `run()` for clean Ctrl+C exit

**Pattern:**
```python
def divide(self, args):
    try:
        a, b = map(int, args.split())
        print(f"Result: {a / b}")
    except ZeroDivisionError:
        print("Can't divide by 0")
    except ValueError:
        print("Invalid numbers.")
```

---

# Phase 2.1 — File I/O + TaskQueue (COMPLETE)

**WHY:** The agent needs to save/load data between sessions. Without this, everything is lost on restart — like a goldfish.

**Key concepts:**
- `with open("file.txt", "w") as f` — open file in write mode, auto-closes when done
- `with open("file.txt", "r") as f` — open file in read mode
- `f.write(string)` — write text to file (strings only, not lists)
- `f.read()` — read entire file as one string
- `.split()` — cut a string into a list at a separator
- Data serialization: choose a format, save in that format, load by splitting at the same format

**Exercise: TaskQueue** — a command pipeline for the agent
- `addTask` — queue up tasks (first-in, first-out)
- `processNext` — pop the first task, identify type ("open ", "run ", "ask "), "execute" it
- `showQueue` / `showProcessed` — numbered list display with `enumerate()`
- `saveQueue` — write queue state to file (name → pending tasks → `---` separator → processed tasks)
- `loadQueue` — read file back, split at separator, reconstruct both lists, handle `FileNotFoundError`
- `run()` — main loop routing: add, next, show, log, save, load, quit

**Key bugs fixed:**
1. `f.write(list)` crashes — must loop and write each item as string + `"\n"`
2. `startswith()` without argument — needs the actual string: `.startswith("open ")`
3. Loading file puts header junk and empty strings into lists — use slicing `[1:-1]` to strip them
4. `pop(firstItem)` wrong — `pop()` needs an index number: `pop(0)`
5. `enumerate(task, i)` — wrong order, it's `for i, task in enumerate(list, 1)`
6. `"ask "[5:]` — "ask " is 4 chars, not 5 → `[4:]`
7. `__init__` had unused parameters `queueList, processedList` → removed them

**Agent connection:** This is the agent's command pipeline. Real agents (AutoGPT, LangChain) queue multiple tasks and process them sequentially. Save/load is how the agent remembers between sessions — conversation history, learned patterns, preferences.

---

## Final Phase 1 Agent (phase1_4.py reference)

Complete working agent with:
- Class-based architecture (`Agent`)
- State management (`self.name`, `self.mode`, `self.isRunning`)
- Mode toggling (chat ↔ voice)
- Command processing (open, run, divide)
- Main loop (quit, toggle, tools, unknown)
- Error handling (KeyboardInterrupt, ZeroDivisionError, ValueError)

## Roadmap Status
- Phase 1 (Python Foundations): DONE
- Phase 2.1 (File I/O - TaskQueue): DONE
- Next: Phase 2.3 — JSON Serialization + Configuration Files

---

# Phase 2.2 — System Control (`os` + `subprocess`) — COMPLETE

**WHY:** The agent needs to *act* on the computer — create folders, navigate, run commands, launch apps. Without this, it can only talk.

**Key concepts:**
- `os` module — talk to the OS: navigate directories, list files, create dirs
  - `os.makedirs(path)` — create nested directories
  - `os.listdir()` — lists items in current directory (think: `ls`/`dir`)
  - `os.getcwd()` — get current working directory (think: `pwd`)
  - `os.chdir(path)` — change directory (think: `cd`)
  - `os.path.abspath(path)` — resolves relative paths to absolute paths
  - `os.path.isdir(path)` — checks if a path is an existing directory
- `subprocess.Popen` — "start and forget" (launch apps that run in background)
- `subprocess.run(capture_output=True, text=True)` — "run and wait" (get command output)
- `shell=True` -- lets the OS shell interpret the command (needed for `echo`, `dir`, app names)
- Nested `dict` for data organization — command metadata (description, aliases, syntax)

**Help system design:** Single method, optional parameter. `help` alone → list all commands. `help <cmd>` → show that command's metadata from the `commands` dict. Extensible pattern.

**Key bugs fixed:**
1. `subprocess.run` vs `Popen` swapped — `start` used blocking `run`, `run` used non-blocking `Popen`. Swapped them.
2. `Popen` returns an object, result has `.stdout` — wrong, `Popen` doesn't capture output like `run` does
3. `find("")` instead of `find(" ")` — empty string always returns `0`
4. `os.getcwd(dir)` — `getcwd` takes no arguments. Used `os.path.abspath(dir)` + `os.getcwd()` comparison instead
5. `help` method defined inside `run()` — not a class method, couldn't access `self.commands` properly
6. `userinput` vs `userInput` — Python is case-sensitive
7. `if content != ""` missing colon
8. `command_name` vs `commandName` — parameter name mismatch
9. `run()` body not indented — all routing code was at class level
10. `os.chdir()` could also raise `NotADirectoryError` — added try/except for `FileNotFoundError`

**Agent connection:** This is the foundation of agent autonomy. Real agents (AutoGPT, Open Interpreter) reason about what the user wants, translate it into OS-level actions (create folders, run scripts, launch tools), and report back. The `os` module gives the agent fingers to navigate. `subprocess` gives it fingers to act.
