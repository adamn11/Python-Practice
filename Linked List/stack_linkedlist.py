class Node(object):
    def __init__(self, value):
        self.value = value
        self.head = None


class Stack(object):
    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def pop(self):
        self.head = self.head.next

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print_list()
    stack.pop()
    stack.print_list()


if __name__ == '__main__':
    main()
