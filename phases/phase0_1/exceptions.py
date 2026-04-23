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
