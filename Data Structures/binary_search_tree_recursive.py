class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.add_helper(self.root, value)
            
    def add_helper(self, start, value):
        if start.value < value:
            if start.right is None:
                start.right = Node(value)
            else:
                self.add_helper(start.right, value)
        else:
            if start.left is None:
                start.left = Node(value)
            else:
                self.add_helper(start.left, value)

    def inorder(self):
        if self.root == None:
            return False
        else:
            self.inorder_helper(self.root)

    def inorder_helper(self, start):
        if start:
            self.inorder_helper(start.left)
            print(start.value)
            self.inorder_helper(start.right)

    def preorder(self):
        if self.root == None:
            return False
        else:
            self.preorder_helper(self.root)

    def preorder_helper(self, start):
        if start:
            print(start.value)
            self.preorder_helper(start.left)
            self.preorder_helper(start.right)

    def postorder(self):
        if self.root == None:
            return False
        else:
            self.postorder_helper(self.root)

    def postorder_helper(self, start):
        if start:
            self.postorder_helper(start.left)
            self.postorder_helper(start.right)
            print(start.value)

    def search(self, value):
        current = self.root

        while current:
            if current.value == value:
                return True
            elif current.value > value:
                current = current.left
            else:
                current = current.right
        return False


t = BinarySearchTree()
t.add(8)
t.add(3)
t.add(10)
t.add(1)
t.add(6)
t.add(14)
t.add(4)
t.add(7)
t.add(13)
t.preorder()
print()
t.inorder()
print()
t.postorder()


