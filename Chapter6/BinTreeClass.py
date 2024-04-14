class BinTNode:
    def __init__(self, data):
        self.data = data
        self.left_c = None
        self.right_c = None
class BinTree:
    def __init__(self):
        self.root = None
    def read(self):
        self.nodes = list(input("請輸入串列形式的節點資料: ").split())
        self.current = 0
        self.root = self.create()
    def readFile(self, fileName):
        fp = open(fileName, "r")
        self.nodes = list(fp.readline().split())
        self.current = 0
        self.root = self.create()
    def create(self):
        nodedata = self.nodes[self.current]
        self.current += 1
        if nodedata == "0":
            return 
        node = BinTNode(nodedata)
        node.left_c = self.create()
        node.right_c = self.create()
        return node
    # def preorder(self, p):
    #     if not p:
    #         return
    #     print(p.data, end = " ")
    #     self.preorder(p.left_c)
    #     self.preorder(p.right_c)
    
t = BinTree()
t.readFile("btree6-7a.txt")
# t.preorder(t.root)