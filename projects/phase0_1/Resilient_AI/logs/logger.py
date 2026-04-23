import logging
import os

# get logger instance
directory_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(directory_path, "app.log")
logger = logging.getLogger(__name__)

logging.basicConfig(
    filemode="a",
    filename=file_path,
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
)
