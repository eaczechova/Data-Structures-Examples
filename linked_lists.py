"""
    Node is an object for storing a single node for a linked list.
    Models two attributes - data and the link to the next node in the list. 
"""

class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = None
    
    def __repr__(self):
        return f"Node data: {self.data}"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return  self.head == None and self.tail == None

    """
    It returns the number of nodes in the list
    It takes O(n) time
    """

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count
    
    """
    Add new Node at the head of the list 
    It takes O(1) time
    """

    def add_to_head(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    """
    Search for the first node containg data that matches the key
    Return the Node or None if not found
    """
    
    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    """
    It inserts new Node containg data at the given index position
    Insertion takes O(1) time, but finding the node takes O(n) time.
    """
    
    def insert(self, data, index):
        if index == 0:
            self.add_to_head(data)
        
        if index > 0:
            new_node = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1
            
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node
                
    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            