# Phase 1.1 — Variables, Types, Input/Output

**Variables** are named containers for data.
**Types** matter — the same operations don't work on all types.

| Type    | Example             | Use in agent                            |
| ------- | ------------------- | --------------------------------------- |
| `str`   | `"hello"`           | All text: prompts, responses, commands  |
| `int`   | `42`                | Counting tokens, retries, loop counters |
| `float` | `0.7`               | Temperature (controls AI creativity)    |
| `bool`  | `True` / `False`    | Mode toggle                             |
| `list`  | `["open", "calc"]`  | Command parts                           |
| `dict`  | `{"name": "Alice"}` | Config, API payloads                    |

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
1. `f.write(list)` crashes — must loop and write each item as string + `"
"`
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

---

# Phase 2.3 — JSON Serialization + Configuration Files (COMPLETE)

**WHY:** The agent needs a clean way to persist and restore settings (name, mode, voice preferences, workspace). Phase 2.1 used manual `---` separators and slicing — JSON replaces that with structured, type-preserving one-line calls.

**Key concepts:**
- `json.dump(obj, file)` — write a Python dict to a file as JSON
- `json.load(file)` — read a JSON file and return a Python dict (types preserved: `true` → `True`, numbers stay numbers)
- `json.dumps(dict)` — dict → string; `json.loads(string)` — string → dict
- Dict `.copy()` — creates a separate copy so mutation of one doesn't affect the other
- Dot-notation keys (`"audio.language"`) → `split(".")` → navigate nested dicts
- `dict.get(key, default)` — safe access with fallback, vs `dict[key]` which crashes on missing keys

**Exercise: ConfigManager** — persistent agent settings
- Defaults dict stored internally, copied to active config on init
- `set_key` — handles both top-level and dot-notation nested keys
- `show_config`, `save_config`, `load_config`, `reset_config`
- Help system reusing the `commands` dict pattern from Phase 2.2
- Clean `run()` loop routing all commands

**Key bugs fixed:**
1. `json.load(dict)` wrong — `json.load` reads from file objects, not dicts
2. `f.write(dict)` crashes — must use `json.dump(dict, f)`
3. `self.config = self.default_config` — no `.copy()` means shared reference, reset breaks
4. Dot-notation parsing in `run()` instead of `set_key()` — user was extracting value from the wrong place
5. `items[dot_pos: + 1:]` — malformed slice, returned empty string
6. `self.config[parts[0][parts[1]]]` — double indexing on wrong object, should be `self.config[parts[0]][parts[1]]`
7. Dot case handled but no `else` branch for flat keys
8. `print(self.help("set"))` — `help` already prints, returns `None` → printed `None`

**Agent connection:** This is the agent's identity layer. Every agent (ChatGPT, Claude, AutoGPT) has a config: system prompt, model, temperature, voice settings. JSON is the universal handoff format — read at startup, write on change, human-editable, type-safe.

---
# Phase 3.1 — HTTP API Client with Conversation History (COMPLETE)

**WHY:** The agent needs to communicate with external LLMs over HTTP. Without this, it's just a local tool — with it, the agent gains a brain. Conversation history enables context across multiple turns.

**Key concepts:**
- `requests.post(url, json=payload)` — send HTTP POST with automatic JSON serialization
- `response.json()` — parse JSON response body into a Python dict
- `response.json()["reply"]` — extract specific field from response dict
- `requests.exceptions.RequestException` — base class for all request errors (connection, timeout, etc.)
- `stream=True` parameter (for future) — yields chunks as they arrive instead of waiting for full response
- Conversation history as `list[dict]` with `{"role": "user|assistant", "content": "..."}` structure
- Inheritance: `ChatAgent(ConfigManager)` accesses parent's `self.config` dict directly
- `super().__init__()` — clean parent constructor call (vs explicit `ConfigManager.__init__(self)`)

**Methods built:**
- `get_reply(user_message)` — appends user msg to history, sends full history to API, applies mock fallback on error, applies assistant reply to history, returns reply string
- `show_status()` — prints current model and endpoint from config
- `clear_history()` — resets `self.history = []`
- `run()` — main loop with command routing: chat messages, clear, status, quit

**Key bugs fixed:**
1. `self.get()` — ConfigManager has no `.get()` method; use `self.config.get(key, default)`
2. f-string quote collision: `f"Model: {self.config.get("model")}"` — inner `"` closes string early, use single quotes inside: `self.config.get('model')`
3. `reply = response.json()` — `json()` returns a dict, not the reply string; need `response.json()["reply"]`
4. Double "Agent: " prefix — `get_reply()` returns a string to `run()`, only print once in `run()`
5. Unnecessary `self.is_running = True` in `__init__` — already inherited from ConfigManager (not wrong, just redundant)
6. Print order: print user message BEFORE calling `get_reply()` so echo appears before potential network delay

**Mock fallback pattern:**
```python
try:
    response = requests.post(url, json=payload, timeout=5)
    reply = response.json()["reply"]
except requests.exceptions.RequestException:
    reply = "LLM server offline."  # programmer-defined fallback
```

**Agent connection:** This is the agent's telephony system. `requests.post()` dials out to the LLM server, `response.json()` receives the answer, `self.history` maintains the call transcript so the LLM remembers what was said. Every AI agent needs this client-server handshake.

---

## Roadmap Status
- Phase 1 (Python Foundations): DONE
- Phase 2.1 (File I/O - TaskQueue): DONE
- Phase 2.2 (System Control - WorkspaceManager): DONE
- Phase 2.3 (JSON + Config - ConfigManager): DONE
- Phase 3.1 (HTTP Client + History): DONE
- Next: Phase 3.2 — Persistent chat memory (save/load history to JSON files)

---

# Supplemental: HTTP Server Deep Dive — How `http.server` Actually Works

**Context**: Building a mock LLM server to test the ChatAgent locally. This is a deep-dive into the mechanics of Python's `http.server` module, written as a first-principles reference.

---

## 1. The Big Picture — What Is an HTTP Server?

An HTTP server is a program that:
1. **Listens** on a network port (e.g., 5000) for incoming connections
2. **Receives** raw bytes from a client (e.g., `requests.post()`)
3. **Parses** those bytes into an HTTP request (method, path, headers, body)
4. **Handles** the request by routing to your handler method
5. **Builds** an HTTP response (status code, headers, body)
6. **Sends** bytes back to the client

Analogy: a receptionist at a building entrance — listens for visitors, reads their note, routes to the right department, writes a reply, hands it back.

---

## 2. Two-Layer Architecture: `HTTPServer` + `BaseHTTPRequestHandler`

- **`HTTPServer`** — the receptionist. Opens a socket, accepts connections, parses the HTTP request line and headers, and dispatches to the handler.
- **`BaseHTTPRequestHandler`** — the department clerk. You subclass it and override `do_GET()`, `do_POST()`, etc. to write request-handling logic.

**Key insight**: You don't write socket code. `HTTPServer` handles networking. You only write the logic inside `do_*` methods.

---

## 3. Request/Response Data Flow, Step-by-Step

### 3.1 What the handler exposes

When a request arrives, your handler instance has:

| Attribute      | Contains                                                     |
| -------------- | ------------------------------------------------------------ |
| `self.path`    | URL path only: `"/api/chat"`                                 |
| `self.command` | HTTP method: `"POST"`, `"GET"`, etc.                         |
| `self.headers` | Dict-like object of all request headers                      |
| `self.rfile`   | File-like **input stream** — read the request body from here |
| `self.wfile`   | File-like **output stream** — write response bytes to here   |

### 3.2 Example incoming HTTP request (raw bytes on wire)

```
POST /api/chat HTTP/1.1

Host: localhost:5000

Content-Type: application/json

Content-Length: 42



{"messages": [{"role": "user", "content": "hi"}]}
```

Breakdown:
- **Request line**: `POST /api/chat HTTP/1.1` → parsed to `self.command='POST'`, `self.path='/api/chat'`
- **Headers**: one per line, `Key: Value` → stored in `self.headers`
- **Blank line** (`
`) → marks end of headers
- **Body**: raw bytes follow → you read from `self.rfile`

---

## 4. Reading the Request Body

```python
content_length = int(self.headers['Content-Length'])  # 42
raw_body = self.rfile.read(content_length)            # reads exactly 42 bytes
body_str = raw_body.decode('utf-8')                   # b'...' → string
data = json.loads(body_str)                           # string → Python dict
```

**Why Content-Length?** TCP gives a byte **stream**, not discrete packets. There's no built-in "end of message" marker. The `Content-Length` header is a contract: "I am sending exactly N body bytes." The server reads exactly N bytes from the stream, then knows the body is complete.

**What `rfile.read(n)` does**:  
`self.rfile` is a `BufferedReader` wrapping the client socket's file descriptor. `read(n)` blocks until exactly `n` bytes arrive (or the socket closes). It returns a `bytes` object.

**Why `.decode('utf-8')`?** Bytes are just numbers. To turn them into readable text, you need an encoding. UTF-8 is the standard for JSON and HTTP.

**What `json.loads()` does**:  
Parses a JSON-formatted string and returns the corresponding Python data structure (dicts, lists, strings, numbers, booleans, None).

---

## 5. Building the Response

```python
self.send_response(200)
self.send_header('Content-Type', 'application/json')
self.send_header('Content-Length', str(len(response_bytes)))
self.end_headers()
self.wfile.write(response_bytes)
```

**Order matters — HTTP response format:** ```
HTTP/1.1 200 OK
                    ← send_response() writes
Content-Type: application/json
      ← send_header() writes
Content-Length: 22
                 ← send_header() writes

                                   ← end_headers() writes (BLANK LINE)
{"reply": "Echo: hi"}                  ← wfile.write() writes
```

- **Status line** (`200 OK`): one-word summary of outcome. Client sees this before parsing anything else.
- **Headers**: metadata that describes the body (`Content-Type` tells how to interpret the bytes, `Content-Length` tells how many bytes to read).
- **Blank line** (`
`): mandatory delimiter. Without it, the client thinks more headers are coming and hangs.
- **Body**: the actual response bytes.

**Why calculate `Content-Length` before sending headers?** Headers must come before the body, but `Content-Length` describes the body's size. So you must:
1. Serialize the body to bytes first
2. Measure it with `len()`
3. Send that number as a header
4. Then send the body

---

## 6. What Each Method Actually Writes

| Method                  | Bytes written to `wfile`  |
| ----------------------- | ------------------------- |
| `send_response(200)`    | `b'HTTP/1.1 200 OK        |
| '`                      |
| `send_header('K', 'V')` | `b'K: V                   |
| '`                      |
| `end_headers()`         | `b'                       |
| '`                      |
| `wfile.write(b'...')`   | `b'...'` (raw body bytes) |

---

## 7. The `BaseHTTPRequestHandler` Dispatch Mechanism

Under the hood:

```python
# Simplified HTTPServer logic
while True:
    client_socket, addr = listen_socket.accept()
    handler = RequestHandlerClass(client_socket, addr, server)
    method = request.command  # "GET", "POST", etc.
    handler_method = getattr(handler, f'do_{method}', None)
    if handler_method:
        handler_method()      # calls your do_POST()
```

Method name `do_POST` is **not arbitrary** — it's a convention. If you define it, `HTTPServer` automatically calls it for POST requests. Same for `do_GET`, `do_PUT`, `do_DELETE`.

---

## 8. What `HTTPServer(...).serve_forever()` Actually Does

```python
server = HTTPServer(('localhost', 5000), ChatHandler)
server.serve_forever()
```

What happens:
1. Creates a TCP listening socket bound to `127.0.0.1:5000`
2. Enters infinite loop:
   - `accept()` — blocks until a client connects → returns `(client_socket, client_addr)`
   - Creates a **fresh** `ChatHandler(client_socket, client_addr, server)` instance (stateless per request)
   - Calls `handler.handle()` → parses request → calls `do_POST()`
   - Closes client socket when handler finishes
3. Repeats

**One handler instance per connection** — not shared between requests. Any state you want to persist must be stored externally (files, database, or a separate session object).

---

## 9. Common Pitfalls

| Symptom              | Cause                                                              |
| -------------------- | ------------------------------------------------------------------ |
| Client hangs forever | Forgot `end_headers()` — blank line never sent                     |
| `json.loads()` error | Body not decoded, or partial read due to wrong `Content-Length`    |
| Empty `data` dict    | Read 0 bytes because `Content-Length` header missing or unparsable |
| Unicode errors       | Sent non-UTF-8 bytes or forgot `.encode('utf-8')` on response      |

---

## 10. Mental Models to Carry Forward

| Model                               | Explanation                                                         |
| ----------------------------------- | ------------------------------------------------------------------- |
| **Server is a loop**                | `serve_forever()` = `while True: accept() → handle() → close()`     |
| **One handler per request**         | Each connection gets a fresh handler instance (stateless by design) |
| **rfile/wfile are streams**         | Read/write like files, but backed by the network socket             |
| **Content-Length = contract**       | "I am sending exactly N bytes." Server reads exactly N.             |
| **JSON is the envelope**            | HTTP carries raw bytes; JSON is the agreed format inside            |
| **`do_*` methods = dispatch table** | Convention: HTTP verb maps to method name                           |

---

# Phase 3.2 — Modular Persistence (COMPLETE)

**WHY:** As the agent grows, a single file becomes a "spaghetti" mess. Decoupling the **Storage Logic** (how data is saved) from the **Interface Logic** (how the user talks) allows the system to scale. This is the transition from a script to a professional **Stateful System**.

**Key concepts:**
- **Inheritance (`class ChatAgent(MemoryManager)`):** The agent "is a" memory manager. It inherits all the saving/loading powers while focusing only on the conversation.
- **State Synchronization:** Ensuring the "Live" variables in Python match the "Physical" data in the `storage.json` file.
- **Bootstrapping:** A startup sequence that checks for existing memory and greets the user differently based on whether it’s a new or returning session.
- **Factory Reset (`clear`):** Wiping the history "silo" while keeping the metadata (like interaction counts) intact.

**Methods built:**
- `MemoryManager.save() / .load()` — The library's heart. Uses `json.dump` and `json.load` to sync the `self.state` dictionary.
- `MemoryManager.clear()` — Resets the `history` list and triggers a save to wipe the disk.
- `ChatAgent.run()` — The controller. Manages the loop, status messages, and command routing.

**Key bugs fixed:**
1. **The "None" Print:** `print(self.save())` resulted in `None` on screen. Fixed by changing `save()` to `return` a success string.
2. **Key Silo Confusion:** `self.state["metadata"]["history"] = []` accidentally nested the history inside metadata. Fixed to `self.state["history"] = []`.
3. **Ghost Variables:** Storing `self.interactions = self.state["metadata"]["total_interactions"]` in `__init__` made the variable static. Fixed by referencing the dictionary directly so the count stays live.
4. **The `elif` Blockade:** Putting the "Resuming..." logic inside the `while` loop caused it to repeat every turn. Fixed by moving the "Bootstrap" check outside the loop.
5. **Scope Death:** Calling `return f.name` outside the `with` block crashed because the file object was closed. Fixed by capturing the name *inside* the block.

---

# Phase 3.3 — Local LLM Integration (COMPLETE)

**WHY:** Moving from "Mock" responses to a real brain. By using **Ollama**, the agent processes the actual conversation history locally, ensuring privacy and real intelligence without subscription fees.

**Key concepts:**
- **The Context Window:** The realization that LLMs are stateless. To "remember," we must send the **entire** `history` list (user and assistant roles) every single time we ask a question.
- **The Request Payload:** Passing `model="llama3.1"` and `messages=self.state["history"]` to the local server.
- **Local Inference:** Using `ollama.chat()` to bridge the Python code to the C++ powered model running on the hardware.

**Logic Loop Update:**
```python
# The "Brain Handshake"
self.add_chat_entry("user", user_input)
response = chat(model="llama3.1", messages=self.state["history"])
bot_txt = response.message.content
self.add_chat_entry("assistant", bot_txt)
self.save() # Persist the memory immediately
```

**Key bugs fixed:**
1. **The "Assisant" Typo:** Misspelling the role key as `"assisant"` caused the LLM to ignore its own previous replies. Fixed to `"assistant"`.
2. **Missing UI Feedback:** The agent felt "frozen" during inference. Fixed by adding a `print("AI is thinking...")` indicator.
3. **Empty Prompting:** Calling the LLM before adding the user's current message to history. Fixed the order: **Input → Update History → Call LLM → Update History → Save.**

---

## Roadmap Status
- Phase 1 (Python Foundations): DONE
- Phase 2 (File I/O & OS Control): DONE
- Phase 3.1 (HTTP & Mock History): DONE
- Phase 3.2 (Modular Persistence): DONE
- Phase 3.3 (Local LLM Integration): DONE
- **Next: Phase 4.1 — The Request/Response Cycle (Networking Deep-Dive)**

---

### **Lessons Learned (The "Mastery" Notes)**
* **Return vs. Print:** Functions that "do work" should `return` a status string so the caller can decide how to show it.
* **Paths Matter:** In a dictionary, `metadata` and `history` are siblings. If you lose track of the path, you lose the data.
* **Memory is a Loop:** An AI doesn't "know" you; it just reads the transcript you give it very, very fast. Keep your transcript clean!


