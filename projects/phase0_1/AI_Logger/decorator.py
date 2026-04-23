from functools import wraps
import time
import logging
import os

DECORATOR_DIR = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(DECORATOR_DIR, "app.log")
# 1. logger configuration
logging.basicConfig(
    level=logging.INFO,
    filename=log_file_path,
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
)

# 2. get an instance
logger = logging.getLogger("AI Logger")


def ai_logger(func):
    @wraps(func)
    def inner(*args, **kwargs):
        function_name = func.__name__
        start_time = time.perf_counter()
        try:
            function_result = func(*args, **kwargs)
            end_time = time.perf_counter()
            duration = end_time - start_time
            logger.info(
                f"SUCCESS: {function_name} | Arguments: {args} | Duration: {duration}s"
            )
        except Exception as e:
            end_time = time.perf_counter()
            duration = end_time - start_time
            logger.error(
                f"ERROR: {function_name} | Arguments: {args} | Error: {e} | Duration: {duration}"
            )
            raise
        return function_result
        # Logs the function name, function args, function result

    return inner
