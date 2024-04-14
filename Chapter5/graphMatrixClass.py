#!/usr/bin/env python
# coding: utf-8

# In[4]:


class GraphMatrix:
    def read(self):
        self.n = int(input("請輸入頂點數： "))
        self.A = [[] for _ in range(self.n)]
        for i in range(self.n):
            self.A[i] = list(map(int, input("請輸入各列元素: ").split()))
    def readFile(self, fileName):
        fp = open(fileName, "r")
        self.n = int(fp.readline())
        self.A = [[] for _ in range(self.n)]
        for i in range(self.n):
            self.A[i] = list(map(int, fp.readline().split()))
    def print(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.A[i][j], end = " ")
            print()
        print()
            
def main():
    g = GraphMatrix()
    g.read()
    #g.readFile("graphArray.txt")
    g.print()

if __name__ == "__main__":
    main()   

