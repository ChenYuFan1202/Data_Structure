#!/usr/bin/env python
# coding: utf-8

# In[2]:


class WtGraph:
    def read(self):
        self.n, self.e = map(int, input("請輸入頂點數和邊數: ").split())
        self.L = [[] for _ in range(self.n)]
        for _ in range(self.e):
            u, v, w = map(int, input("請輸入每個邊的起點、終點、權重: ").split())
            self.L[u].append((v, w))
    def readFile(self, fileName):
        fp = open(fileName, "r")
        self.n, self.e = map(int, fp.readline().split())
        self.L = [[] for _ in range(self.n)]
        for _ in range(self.e):
            u, v, w = map(int, fp.readline().split())
            self.L[u].append((v, w))
    def print(self):
        for i in range(self.n):
            print(self.L[i])
        print()

def main():
    g1 = WtGraph()
    g2 = WtGraph()
    g1.read()
    g2.readFile("wtGraphList.txt")
    g1.print()
    g2.print()
    
if __name__ == "__main__":
    main()

