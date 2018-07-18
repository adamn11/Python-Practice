# Implemented using Doubly Linked List
class Node(object):
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    # Enqueue from head
    def enqueue(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Dequeue from tail
    def dequeue(self):
        self.tail = self.tail.prev
        self.tail.next = None

    def show(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
        print('')


def main():
    list = LinkedList()
    list.enqueue(1)
    list.enqueue(2)
    list.enqueue(3)
    list.show()
    list.dequeue()
    list.show()
    list.dequeue()
    list.show()


if __name__ == '__main__':
    main()
