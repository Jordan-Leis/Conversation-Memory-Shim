class ConversationMemoryShim:
    """Simple memory that stores user constraints to avoid repeat questions."""

    def __init__(self):
        self.constraints = {}

    def add_constraint(self, key: str, value: str):
        """Store a constraint with a key."""
        self.constraints[key] = value

    def get_constraint(self, key: str):
        """Retrieve a stored constraint or None."""
        return self.constraints.get(key)

    def has_constraint(self, key: str) -> bool:
        return key in self.constraints
