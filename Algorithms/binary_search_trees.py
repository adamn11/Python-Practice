'''

Binary Search Tree:

Time Complexity:
Space Complexity:

Implementation:
insert
remove
in-order (iteratively and recursively)
post-order (iteratively and recursively)
pre-order (iteratively and recursively)

'''

class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None


class Binary_Search_Tree:
    def __init__(self):
        self.root = None

    def insert_helper(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.insert(self.root, value)
    
    def insert(self, position, value):
        if value < position.value:
            if position.left == None:
                position.left = Node(value)
            else:
                return self.insert(position.left, value)
        else:
            if position.right == None:
                position.right = Node(value)
            else:
                return self.insert(position.right, value)

    def print(self, position):
        if position:
            self.print(position.left)
            print(position.value)
            self.print(position.right)

    def print_helper(self):
        self.print(self.root)


def main():
    t = Binary_Search_Tree()
    t.insert_helper(1)
    t.insert_helper(3)
    t.insert_helper(2)
    t.insert_helper(7)
    t.insert_helper(9)
    t.insert_helper(6)
    t.print_helper()

if __name__ == '__main__':
    main()