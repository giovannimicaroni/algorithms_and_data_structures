class HashTable:
    """Simple hash table with separate buckets for collision handling."""
    
    def __init__(self, size: int = 10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0
    
    def _hash(self, key):
        """
        Hash function: convert key to bucket index. Returns bucket index (1 to size-1).
        """
        return hash(key) % self.size
    
    def set_pair(self, key, value):
        """
        Insert or update key-value pair.
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
        self.count += 1
    
    def get(self, key, default=None):
        """
        Retrieve value by key. Returns value associated with key, or a default value if not found.
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return default
    
    def remove(self, key):
        """
        Remove key-value pair by key.
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.count -= 1
                return
        
        raise KeyError(f"Key {key} not found")
    
    def contains(self, key):
        """
        Check if key exists. Returns key if it exists. Otherwise, returns None.
        """
        return self.get(key) is not None
    
    def __len__(self):
        """Return number of key-value pairs."""
        return self.count
    
    def __getitem__(self, key):
        """Access via bracket notation: ht[key]."""
        value = self.get(key)
        if value is None:
            raise KeyError(f"Key {key} not found")
        return value
    
    def __setitem__(self, key, value):
        """Set via bracket notation: ht[key] = value."""
        self.set(key, value)
    
    def __contains__(self, key):
        """Check membership: key in ht."""
        return self.contains(key)
    
    def keys(self):
        """Return all keys."""
        keys = []
        for bucket in self.table:
            for k, v in bucket:
                keys.append(k)
        return keys
    
    def values(self):
        """Return all values."""
        values = []
        for bucket in self.table:
            for k, v in bucket:
                values.append(v)
        return values
    
    def items(self):
        """Return all (key, value) pairs."""
        items = []
        for bucket in self.table:
            for k, v in bucket:
                items.append((k, v))
        return items