class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
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
        if self.root is None:
            return False
        else:
            self.inorder_helper(self.root)

    def inorder_helper(self, start):
        if start:
            self.inorder_helper(start.left)
            print(start.value)
            self.inorder_helper(start.right)

    def preorder(self):
        if self.root is None:
            return False
        else:
            self.preorder_helper(self.root)

    def preorder_helper(self, start):
        if start:
            print(start.value)
            self.preorder_helper(start.left)
            self.preorder_helper(start.right)

    def postorder(self):
        if self.root is None:
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

    def bfs(self):
        queue = [self.root]

        while queue:
            popped = queue.pop(0)
            print(popped.value)
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)

    def dfs(self):
        stack = [self.root]

        while stack:
            popped = stack.pop()
            print(popped.value)
            if popped.right:
                stack.append(popped.right)
            if popped.left:
                stack.append(popped.left)

    def is_symmetrical(self):
        if self.root is None:
            return False

        return self.is_symmetrical_helper(self.root.left, self.root.right)

    def is_symmetrical_helper(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return self.is_symmetrical_helper(t1.left, t2.right) and \
               self.is_symmetrical_helper(t1.right, t2.left)


first = BinarySearchTree()
first.add(4)
first.add(3)
first.add(5)
first.add(1)
first.add(7)
first.bfs()
print(first.is_symmetrical())


