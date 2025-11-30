class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next_node = None

class SinglyLinkedList():
    '''
    Implementation of a simple Singly Linked List class with tail pointer. Provides methods to insert, remove and search nodes. Also keeps track of list length.
    Other useful methods could be implemented. For now, I'll provide only these.
    '''
    def __init__(self, head: LinkedListNode = None):
        self.head = head
        self.tail = head
        self.length = 1 if head is not None else 0
    
    def __str__(self):
        '''
        Returns string representation of the linked list.
        '''
        values = []
        current_node = self.head
        while current_node is not None:
            values.append(str(current_node.value))
            current_node = current_node.next_node
        return " -> ".join(values) + " -> None"

    def insert_node_beginning(self, node):
        '''
        Inserts node at beginning of the linked list. Time complexity: O(1)
        '''
        if node is None:
            raise ValueError("Cannot add None to the list")
        
        node.next_node = self.head
        self.head = node
        self.length += 1
        
        if self.length == 1:
            self.tail = node

    def delete_node_beginning(self):
        '''
        Removes the first node of the list and returns its value. Time complexity: O(1)
        '''
        if self.head is None:
            raise IndexError("Cannot delete from an empty list")
        
        first_node = self.head
        self.head = self.head.next_node
        first_node.next_node = None
        self.length -= 1
        
        if self.length == 0:
            self.tail = None

        return first_node.value
    
    def insert_node_end(self, node):
        '''
        Inserts node at end of the linked list. Time complexity: O(1)
        '''
        if node is None:
            raise ValueError("Cannot add None to the list")
        
        node.next_node = None
        self.length += 1
        
        if self.head is None:
            self.head = node
            self.tail = node
            return
        
        self.tail.next_node = node
        self.tail = node
    
    def delete_node_end(self):
        '''
        Removes the last node of the list and returns its value. Time complexity: O(n)
        '''
        if self.head is None:
            raise IndexError("Cannot delete from an empty list")
        
        last_node = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return last_node.value

        current_node = self.head
        while current_node.next_node is not self.tail:
            current_node = current_node.next_node
        
        current_node.next_node = None
        self.tail = current_node
        self.length -= 1
        return last_node.value
    
    def search(self, value):
        '''
        Searches for a node with the given value. Time complexity: O(n)
        Returns the node if found, None otherwise.
        '''
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return current_node
            current_node = current_node.next_node
        
        return None

        

