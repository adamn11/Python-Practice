class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None

    def add_front(self, data):
<<<<<<< HEAD
        node = Node(data)
        node.next = self.head
        self.head = node
=======
        node = Node(data, None)  # Create new node instance storing a value
        node.next = self.head  # Set new node's next to reference old head node
        self.head = node  # Set variable head to reference the new node
>>>>>>> origin/master

    def add_back(self, data):
        current = self.head
        previous = None

        while current:
            previous = current
            current = current.next

        node = Node(data)
        previous.next = node

    # Catch if index[0]
    def add(self, data, index):
        current = self.head
        previous = None
        counter = 0

        while counter < index:
            previous = current
            current = current.next
            counter += 1

        node = Node(data)
        node.next = current
        previous.next = node

    def delete(self, data):
        current = self.head
        previous = None

        while current:
            if current.value == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True

            previous = current
            current = current.next
        return False

    def get_size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        print("Size of list is: " + str(count))

    def show_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
        print("\n")


def main():
    list = SinglyLinkedList()
    list.add_front(3)
    list.add_front(2)
    list.add_front(1)

    list.show_list()
    list.get_size()

    list.add(1, 1)
    list.show_list()
    list.get_size()

    list.delete(2)
    list.show_list()

    list.add_back(4)
    list.show_list()


if __name__ == '__main__':
    main()
