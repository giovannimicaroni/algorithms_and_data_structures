class Stack():
    """LIFO stack backed by a Python list."""

    def __init__(self):
        self.stack = []

    def push(self, value):
        """Push value onto the stack."""
        self.stack.append(value)
        return

    def pop(self):
        """Pop and return the top value. Raises IndexError if empty."""
        if not self.stack:
            raise IndexError("pop from empty Stack")
        return self.stack.pop()
    
    def peek(self):
        """Return the top value without removing it. Raises IndexError if empty."""
        if not self.stack:
            raise IndexError("pop from empty Stack")
        return self.stack[-1]
    
    def is_empty(self):
        """Return True if stack is empty."""
        return len(self.stack) == 0
    
    def __len__(self):
        """Return number of elements (called by len(obj))."""
        return len(self.stack)
    
    def __repr__(self):
        """Debug representation (called by repr(obj), REPL, containers and replaces str if str is absent)."""
        return f"Stack({self.stack!r})"