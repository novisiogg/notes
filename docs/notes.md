## Phase 0.1 — [Python Language Deep Dive]

## Core Concepts & Patterns
- **Pathlib Manager:** Moved from string-based paths to pathlib.Path objects.
- **Encodings:** *UnicodeDecodeError* by enforcing *utf-8* encoding.
- **Resource Management (Context Managers):** Implemented the *@contextmanager* to create context managers.
- **Generators (yield):** Used generators to implement memory-efficient data streaming.
- **Package Structure & Imports:** Managed Python's module resolution by updating *sys.path* to enable imports across project directories.
- **Dependency Injection:** Refractored functions to accept external configurations (like *log_path*) instead of hardcoding them.

## Code Patterns & Snippets
### `phases\phase0_1\context_managers.py`
```python
@contextmanager
def MultiResourceManagerTwo(filenames: list):
    mounted_files = []

    try:
        # 🔧 setup phase (like __enter__)
        for filename in filenames:
            if filename == "CRITICAL_FAIL":
                print("CRITICAL_FAIL: Mounting aborted. Rolling back...")
                raise RuntimeError("Mounting failed")
            mounted_files.append(filename)

        yield mounted_files  # 👈 what `as` receives

    finally:
        # 🧹 cleanup on failure
        for name in reversed(mounted_files):
            print(f"SYSTEM SECURED: Unmounting {name}...")


with MultiResourceManagerTwo(["db.bin", "config.json", "CRITICAL_FAIL"]) as manager:
    print(manager)
```

### `phases\phase0_1\decorators.py`
```python
def measure_time(func):
    @wraps(func)
    def inner(*args, **kwargs):
        function_name = func.__name__
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"[TIMER]: {function_name} took [{-start_time + end_time}] seconds to execute."
        )
        return result

    return inner
```

### `phases\phase0_1\exceptions.py`
```python
class InvalidInferenceConfig(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code


def load_config(status: str):
    if status.upper() != "READY":
        raise InvalidInferenceConfig("[ALERT] Change status to 'READY'", 404)
    else:
        print("Hi there.")


try:
    load_config("ready")
except InvalidInferenceConfig as e:
    print("Caught an error", e)
finally:
    print("[SYSTEM]: Config check complete.")
```

### `phases\phase0_1\generators.py`
```python
# [expression for item in iterable if condition] - List comprehensions
names_list = ["novisiogg", "zouma", "tyx", "regedit"]
# removes name if it's not "novisiogg"
res = [names_list.remove(name) for name in reversed(names_list) if name != "novisiogg"] # reversed since we're updating the list in a loop

# {key_expression: value_expression for item in iterable if condition} - Dictionary comprehension
first_names = ["novisio", "zouma", "tyx"]
last_names = ["gg", "games", "maftouh"]

another_result = {a: b for a, b in zip(first_names, last_names)}
print(another_result)

# {expression for item in iterable if condition} - Set comprehensions (same as List)

l = [1, 1, 3, 2, 5, 6]
reslt = {num**2 for num in l}
```

## Exercises/Projects Done
* [AI_Logger](../projects/phase0_1/AI_Logger)
* [Data_Streaming](../projects/phase0_1/Data_Streaming)
* [Resilient_AI](../projects/phase0_1/Resilient_AI)
* [Resource_Monitor](../projects/phase0_1/Resource_Monitor/)
---