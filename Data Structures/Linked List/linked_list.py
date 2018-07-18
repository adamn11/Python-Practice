class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None

    def add_front(self, data):
        node = Node(data, None)  # Create new node instance storing a value
        node.next = self.head  # Set new node's next to reference old head node
        self.head = node  # Set variable head to reference the new node

    def add(self, data, index):
        current = self.head
        previous = None
        counter = 0

        while counter < index:
            previous = current
            current = current.next
            counter += 1

        node = Node(data, None)
        node.next = current
        previous.next = node

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current is not None and found is False:
            if current.value == data:
                found = True
            else:
                previous = current
                current = current.next
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def get_size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        print("Size of list is: " + str(count))

    def show_list(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next


def main():
    list = SinglyLinkedList()
    list.add_front(1)
    list.add_front(2)
    list.add_front(3)

    list.show_list()
    list.get_size()

    list.add(0, 3)
    list.show_list()
    list.get_size()

    list.delete(2)
    list.show_list()

if __name__ == '__main__':
    main()
