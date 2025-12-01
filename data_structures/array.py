import ctypes

class Array:
    """"
    Python implementation of a class that functions like a C array.
    Contains essential methods for it's manipulation and use. Uses ctypes to create low-level C arrays
    """
    def __init__(self, size: int):
        self.length = 0
        self._size = size
        self._array = self._make_array(self._size)
    
    def _make_array(self, c: int):
        """Allocate a ctypes array of PyObject* with c slots."""
        return (c * ctypes.py_object)()
    
    def __len__(self):
        """Return number of stored elements."""
        return self.length
    
    def __getitem__(self, k: int):
        """Return item at index k."""
        if not 0 <= k < self.length:
            raise IndexError("index out of range")
        return self._array[k]

    def __iter__(self):
        """Iterate over stored elements."""
        for i in range(self.length):
            yield self._array[i]
    
    def append(self, value):
        """Append value to the end (resize if needed)."""
        if self.length == self._size:
            self._resize(2 * self._size)
        self._array[self.length] = value
        self.length += 1
    
    def pop(self):
        """Remove and return the last element."""
        if self.length == 0:
            raise IndexError("pop from empty")
        value = self._array[self.length-1]
        self.length -= 1
        return value

    def _resize(self, new_size: int):
        """Resize underlying buffer to new_size."""
        B = self._make_array(new_size)
        for i in range(self.length):
            B[i] = self._array[i]
        self._array = B
        self._size = new_size
        
