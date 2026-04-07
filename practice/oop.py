# classe

class SecretKey:
    def __init__(self, owner, value):  # type: ignore
        # This just saves the data when you create the object
        self.owner = owner
        self.value = value

    # 1. THE LABEL (For humans/users)
    def __str__(self):
        return f"Key belongs to: {self.owner}"

    # 2. THE INSTRUCTIONS (For you, the coder)
    def __repr__(self):
        return f"SecretKey(owner='{self.owner}', value='{self.value}')"

# --- ACTUALLY USING IT ---
my_key = SecretKey("novisio", "ABC-123")