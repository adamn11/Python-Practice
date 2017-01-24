# Implemented using Doubly Linked List
class Node:
    def __init(self, value=None, prev = None, next=None):
        self.value = value
        self.prev = None
        self.next = None

    def get_value(self):
        return self.value

    def get_prev(self):
        return self.prev

    def get_next(self):
        return self.next

    def set_value(self, data):
        self.value = data

    def set_prev(self, data):
        self.prev = data

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Enqueue from head
    def enqueue(self, data):
        new_node = Node(data,None,None)
        # If list is empty, replace with is_empty
        if self.head == None
            self.head = self.tail = new_node
        new_node.set_next(self.head)
        self.head.prev = new_node
        self.head = new_node

    # Dequeue from tail
    #def dequeue(self):

    #def is_empty(self):


def main():
    list = LinkedList()

if __name__ == '__main__':
    main()
