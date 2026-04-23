class MultiResourseManager:
    def __init__(self, filenames: list):
        self.filenames = filenames
        self.mounted_filenames = []

    def __enter__(self):
        for filename in self.filenames:
            if filename == "CRITICAL_FAIL":
                print("CRITICAL_FAIL: Mounting aborted. Rolling back...")
                raise RuntimeError("Mounting failed")
            self.mounted_filenames.append(filename)
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type is RuntimeError:
            for name in reversed(self.mounted_filenames):
                print(f"SYSTEM SECURED: Unmounting {name}...")
            self.mounted_filenames.clear()
            return True
        return False


with MultiResourseManager(["db.bin", "config.json", "CRITICAL_FAIL"]) as manager:
    print(manager)
    print(manager.mounted_filenames)
print("Program continued execution successfully!")
