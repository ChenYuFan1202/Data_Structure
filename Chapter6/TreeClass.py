class Tree:
    def read(self):
        self.n = int(input("請輸入樹的總節點數：　"))
        self.L = [[] for _ in range(self.n)]
        for _ in range(self.n - 1):
            i, j = map(int, input("請輸入i和j: ").split())
            self.L[i].append(j)

    def readFile(self, fileName):
        fp = open(fileName, "r")
        self.n = int(fp.readline())
        self.L = [[] for _ in range(self.n)]
        for _ in range(self.n - 1):
            i, j = map(int, fp.readline().split())
            self.L[i].append(j)

    def print(self):
        for i in range(self.n):
            print("{}:{}".format(i, self.L[i]))
        print()

    def findRoot(self):
        indegree = [0] * self.n
        for u in range(self.n):
            for v in self.L[u]:
                indegree[v] += 1
        return indegree.index(0)

if __name__ == "__main__":
    t = Tree()
    t.readFile("tree6-1.txt")
    t.print()