class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class binary:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self.insert_recur(value, self.root)

    def insert_recur(self, value, curr):
        if curr is None:
            return node(value)
        elif curr.value < value:
            curr.right = self.insert_recur(value, curr.right)
        elif curr.value > value:
            curr.left = self.insert_recur(value, curr.left)
        return curr

    def trans(self):
        self.print_trans(self.root)

    def print_trans(self, node):
        if node is None:
            return
        self.print_trans(node.left)
        print("----->", node.value,end=" ")
        self.print_trans(node.right)

tree = binary()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)

tree.trans()
