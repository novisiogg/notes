import logging
import psutil
import os
import time
from pathlib import Path
from contextlib import contextmanager

log_file_path = Path("projects/phase0_1/Resource_Monitor") / "resources.log"
# Gets an instance of logger
logger = logging.getLogger("Resource Monitor")
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
)


@contextmanager
def resource_monitor(label):
    # Gets the process
    process = psutil.Process(os.getpid())
    # Gets the memory, and time before the script
    memory_before = process.memory_info().rss
    time_before = time.perf_counter()

    try:
        yield
    except Exception as e:
        logger.error(f"[{label}] Error occured. {e}")
        raise

    finally:
        # Gets the memory, and time after the script
        memory_after = process.memory_info().rss
        time_after = time.perf_counter()
        # Gets memory usage
        delta = memory_after - memory_before
        # Gets duration
        duration = time_after - time_before
        # Converts memory to MB
        delta_mb = delta / (1024 * 1024)
        logger.info(
            f"[{label}] Memory Delta: {delta_mb:.2f}MB | Time Elapsed: {duration:.2f}s"
        )
