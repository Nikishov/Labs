class TreeNode:
    def __init__(self, value):
        self.value  = value
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value:
            if data < self.value:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.value:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.value = data

    def find_minimum(self, node):
        if node.left == None:
            return node
        return self.find_minimum(node.left)

    def find_maximum(self, node):
        if node.right == None:
            return node
        return self.find_maximum(node.right)

    def find_element(self, value):
        if value < self.value:
            if self.left is None:
                print(str(value) + ' не найден')
            return self.left.find_element(value)
        elif value > self.value:
            if self.right is None:
                print(str(value) + ' не найден')
            return self.left.find_element(value)
        else:
            print(str(value) + ' найден')

    def delete(self, root, z):
        if root == None:
            return root
        if z < root.value:
            root.left = self.delete(root.left, z)
        elif z > root.value:
            root.right = self.delete(root.right, z)
        elif root.left and root.right:
            root.value = self.find_minimum(root.right).value
            root.right = self.delete(root.right, root.value)
        else:
            if root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                root = None
        return root

    def pre_order(self, node):
        if node:
            print(node.value)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.value)
            self.in_order(node.right)

tree = TreeNode(10)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(50)
tree.delete(tree, 2)
tree.find_element(10)
tree.pre_order(tree)