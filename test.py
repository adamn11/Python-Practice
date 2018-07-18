class Node(Object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(Object):
    def __init__(self):
        self.tail = None


def add_tail(self, value):
    node = Node(value)  # Create new node with value
    node.next = None  # Set the node's next reference to None
    self.tail.next = node  # Set the tail's next reference to the new node
    self.tail = node  # Set the tail to reference the new node

