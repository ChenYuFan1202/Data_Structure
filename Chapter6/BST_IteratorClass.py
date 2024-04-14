from BSTClass import *
class BST_Iterator:
    def __init__(self, root):
        self.nodes = []
        self.inorder(root)
        self.current = 0
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left_c)
        self.nodes.append(node.data)
        self.inorder(node.right_c)
    def next(self):
        nodedata = self.nodes[self.current]
        self.current += 1
        return nodedata
    def hasNext(self):
        return self.current < len(self.nodes)
    
# t = BST()
# t.createFromFile("bst6-28.txt")
# obj = BST_Iterator(t.root)
# print(obj.next())
# print(obj.next())
# print(obj.hasNext())