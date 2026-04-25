import ollama
import sys
from pathlib import Path

# Identify project root (where the 'projects' folder lives)
# Assuming 'main.py' is inside 'projects/phase0_1/Data_Streaming/'
# Go up 3 levels to reach the directory containing 'projects/'
project_root = Path(__file__).resolve().parents[2]

# Add that root to Python's search path
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from phase0_1.Resource_Monitor.resource_monitor import resource_monitor

batch_file = (
    Path(r"C:\Users\vwu\Desktop\notes\projects\phase0_1\Data_Streaming\batch")
    / "ROADMAP.md"
)

log_path = Path(__file__).resolve().parent / "resources.log"


def ollama_call(batch):
    text = "".join(batch)
    response = ollama.chat(
        model="llama3.1", messages=[{"role": "user", "content": text}]
    )
    return response


def implement_batch(file, batch_size=100):
    if file.exists():
        with open(file, "r", encoding="utf-8") as f:
            batch = []
            for line in f:
                batch.append(line)
                if len(batch) == batch_size:
                    yield batch
                    batch = []
            if batch:
                yield batch
    else:
        print("File not found.")


with resource_monitor("Batch Streaming", log_path):
    my_stream = implement_batch(batch_file, 100)
    for i, batch in enumerate(my_stream):
        try:
            ollama_call(batch)
            print(f"Successfully processed batch {i}")
        except Exception as e:
            print(f"Failed on batch {i}, {e}")
