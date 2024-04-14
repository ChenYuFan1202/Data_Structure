class BinTNode:
    def __init__(self, data):
        self.data = data
        self.left_c = None
        self.right_c = None
class BST:
    def __init__(self):
        self.root = None
    def create(self):
        self.nodes = list(input("請輸入串列形式的節點資料: ").split())
        for nodedata in self.nodes:
            node = BinTNode(nodedata)
            self.insert(node)
    def insert(self, newnode):
        LEFT, RIGHT = range(2)
        if not self.root:
            self.root = newnode
        current = self.root
        while current:
            curParent = current
            if newnode.data < current.data:
                current = current.left_c
                direction = LEFT
            elif newnode.data > current.data:
                current = current.right_c
                direction = RIGHT
            else:
                return
        if direction == LEFT:
            curParent.left_c = newnode
        else:
            curParent.right_c = newnode
    def createFromFile(self, fileName):
        fp = open(fileName, "r")
        self.nodes = list(fp.readline().split())
        for nodedata in self.nodes:
            node = BinTNode(nodedata)
            self.insert(node)
    def preorder(self, p):
        if not p:
            return
        print(p.data, end = " ")
        self.preorder(p.left_c)
        self.preorder(p.right_c)
    def inorder(self, p):
        if not p:
            return
        self.inorder(p.left_c)
        print(p.data, end = " ")
        self.inorder(p.right_c)
    def postorder(self, p):
        if not p:
            return
        self.postorder(p.left_c)
        self.postorder(p.right_c)
        print(p.data, end = " ")
    def search(self, key):
        current = self.root
        while current:
            if key < current.data:
                current = current.left_c
            elif key > current.data:
                current = current.right_c
            else:
                return True
        return False        

# t = BST()
# t.createFromFile("bst6-28.txt")
# t.preorder(t.root)
# print()
# key = input("請輸入key: ")
# print(t.search(key))

# class BinTNode:
#     def __init__(self, data):
#         self.data = data
#         self.left_c = None
#         self.right_c = None
# class BST:
#     def __init__(self):
#         self.root = None
#     def create(self):
#         self.nodes = list(input("請輸入串列形式的節點資料: ").split())
#         for nodedata in self.nodes:
#             node = BinTNode(nodedata)
#             self.insert(node)
#     def insert(self, newnode):
#         LEFT, RIGHT = range(2)
#         if not self.root:
#             self.root = newnode
#             return
#         current = self.root
#         while current:
#             curParent = current
#             if newnode.data < current.data:
#                 direction = LEFT
#                 current = current.left_c
#             elif newnode.data > current.data:
#                 direction = RIGHT
#                 current = current.right_c
#             else:
#                 return
#         if direction == LEFT:
#             curParent.left_c = newnode
#         else:
#             curParent.right_c = newnode
#     def createFromFile(self, fileName):
#         fp = open(fileName, "r")
#         self.nodes = list(fp.readline().split())
#         for nodedata in self.nodes:
#             node = BinTNode(nodedata)
#             self.insert(node)
#     def preorder(self, p):
#         if not p:
#             return
#         print(p.data, end = " ")
#         self.preorder(p.left_c)
#         self.preorder(p.right_c)
#     def inorder(self, p):
#         if not p:
#             return
#         self.inorder(p.left_c)
#         print(p.data, end = " ")
#         self.inorder(p.right_c)
#     def postorder(self, p):
#         if not p:
#             return
#         self.postorder(p.left_c)
#         self.postorder(p.right_c)
#         print(p.data, end = " ")
#     def search(self, key):
#         current = self.root
#         while current:
#             if key < current.data:
#                 current = current.left_c
#             elif key > current.data:
#                 current = current.right_c
#             else:
#                 return True
#         return False