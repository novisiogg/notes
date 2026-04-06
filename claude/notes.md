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

## Final Phase 1 Agent (phase1_4.py)

Complete working agent with:
- Class-based architecture (`Agent`)
- State management (`self.name`, `self.mode`, `self.isRunning`)
- Mode toggling (chat ↔ voice)
- Command processing (open, run, divide)
- Main loop (quit, toggle, tools, unknown)
- Error handling (KeyboardInterrupt, ZeroDivisionError, ValueError)

## Roadmap Status
- Phase 1 (Python Foundations): DONE
- Next: Phase 2 — System Control (file I/O, OS, subprocess, automation)
- Notes saved to: C:\Users\vwu\Desktop\notes\claude\notes.md
