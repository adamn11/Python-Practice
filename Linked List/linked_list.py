class Node:
    def __init__(self,value = None, next = None):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_value(self,data):
        self.value = data

    def set_next(self,new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data): # Adding at the front of the list
        node = Node(data, None)
        node.set_next(self.head)
        self.head = node

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current is not None and found is False:
            if current.get_value() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def get_size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        print "Size of list is: " + str(count)

    def show_list(self):
        current = self.head
        while current is not None:
            print current.get_value()
            current = current.get_next()

def main():
    list = LinkedList()
    list.add(1)
    list.add(2)
    list.add(3)

    list.show_list()
    list.get_size()

    list.delete(2)
    list.show_list()

if __name__ == '__main__':
    main()
