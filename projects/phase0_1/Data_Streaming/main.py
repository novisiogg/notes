import ollama
import sys
import os
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
    / "large_file.txt"
)

log_path = Path(__file__).resolve().parent / "resources.log"


if batch_file.exists():
    print("file already exists. not writing anything to it")
else:
    with open(batch_file, "w", encoding="utf-8") as f:
        for i in range(1_000_000):
            f.write(f"Line {i}. This is dummy data.\n")


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
    for batch in my_stream:
        print(f"DEBUG: Just received a batch of a {len(batch)}")


def simple_return(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            return lines
    except:
        print("File not found.")


with resource_monitor("Simple Streaming", log_path):
    lines = simple_return(batch_file)
    print(f"DEBUG: Simple Streaming loaded {len(lines)} lines into memory.")
