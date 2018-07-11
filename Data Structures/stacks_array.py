class Stack:
    def __init__(self):
        self.data = []

    def len(self):
        return len(self.data)

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def peek(self):
        if len(self.data) != 0:
            return self.data[-1]

    def print(self):
        print(self.data)


def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.peek())
    s.print()
    s.pop()
    s.print()
    s.pop()
    s.print()

if __name__ == "__main__":
    main()
