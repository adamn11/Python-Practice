class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def add_front(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def add_back(self, data):
        current = self.head
        previous = None

        while current:
            previous = current
            current = current.next

        node = Node(data)
        previous.next = node


    def add_target(self, data, target):
        current = self.head
        previous = None
        counter = 0

        while counter < target:
            previous = current
            current = current.next
            counter = counter + 1

        node = Node(data)
        node.next = current
        previous.next = node

    def print_list(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next

        print("\n")

    def delete(self, target_data):
        current = self.head
        previous = None

        while current:
            if current.data == target_data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True

            previous = current
            current = current.next

        return False


def main():
    list = LinkedList()
    list.add_front(6)
    list.add_front(4)
    list.add_front(2)
    list.print_list()
    list.add_target(5, 2)
    list.print_list()
    list.add_target(3, 1)
    list.print_list()
    list.delete(5)
    list.print_list()
    list.add_back(7)
    list.print_list()


if __name__ == '__main__':
    main()
