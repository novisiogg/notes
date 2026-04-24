import json
from pathlib import Path
from projects.phase0_1.Resilient_AI.logs.logger import logger

file_path = Path("projects/phase0_1/Resilient_AI/memory") / "history.json"


class MemoryManager:
    def __init__(self, filename=file_path):
        self.filename = filename
        self.state = {}

    def _default_state(self):
        return {
            "metadata": {"interactions": 0},
            "history": [
                {
                    "role": "system",
                    "content": "You are a witty, helpful AI assistant named Stiwert.",
                }
            ],
        }

    def load_history(self):
        if self.filename.exists():
            try:
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    self.state = data
                    logger.info("Successfully loaded state from file.")
            except (FileNotFoundError, json.JSONDecodeError):
                logger.error("Couldn't load history. File corrupted or does not exist.")
                self.state = self._default_state()
        else:
            self.state = self._default_state()
            logger.info("Successfully loaded fresh state.")

    def save_history(self):
        try:
            with open(self.filename, "w") as f:
                json.dump(self.state, f, indent=2)
                logger.info("Successfully saved history to file.")
        except Exception as e:
            logger.error(
                f"Couldn't save to file. File corrupted or does not exist. {e}"
            )
            raise

    def clear_history(self):
        self.state = self._default_state()
        logger.info("Successfully cleared history.")
        self.save_history()

    def increment_interactions(self):
        self.state["metadata"]["interactions"] += 1
        logger.info("New interaction.")

    def add_messages(self, role, content):
        messages = {"role": role, "content": content}
        self.state.setdefault("history", []).append(messages)
        self.save_history()
        logger.info(f"New messages added | Role: {role} | Content: {content}")
