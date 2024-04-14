#!/usr/bin/env python
# coding: utf-8

# In[3]:


class GraphList:
    def read(self):
        self.n, self.e = map(int, input("請輸入頂點數和邊數: ").split())
        self.L = [[] for _ in range(self.n)]
        for _ in range(self.e):
            i, j = map(int, input("請輸入每個邊的起點和終點: ").split())
            self.L[i].append(j)
#         print(self.L)
    def readFile(self, fileName):
        fp = open(fileName, "r")
        self.n, self.e = map(int, fp.readline().split())
        self.L = [[] for _ in range(self.n)]
        for _ in range(self.e):
            i, j = map(int, fp.readline().split())
            self.L[i].append(j)
#         print(self.L)
        
    def print(self):
        for i in range(self.n):
            print(self.L[i])
        print()
        
def main():
    g = GraphList()
    # g.read()
    g.readFile("graphList.txt")
    g.print()

if __name__ == "__main__":
    main()


