#!/usr/bin/env python
# coding: utf-8

# In[2]:


maxSize = 10000
class Stack:
    def __init__(self, maxsize = maxSize):
        self._maxsize = maxSize
        self._item = [0] * self._maxsize
        self._top = -1
    def isEmpty(self):
        if self._top < 0:#== -1?
            return True
        else:
            return False
    def isFull(self):
        if self._top >= self._maxsize - 1:#len(self._item)不行，是因為全部都用0來代替了
            return True
        else:
            return False
    def push(self, value):
        if not self.isFull():
            self._top += 1
            self._item[self._top] = value
    def pop(self):
        if not self.isEmpty():
            popped = self._item[self._top]
            self._top -= 1
            return popped
        return None
    def peek(self):
        if not self.isEmpty():
            return self._item[self._top]
        return None
    def print(self):#bottom up
        for i in range(self._top + 1):
            print(self._item[i], end = " ")
        print()
        
def main():
    a = Stack()
    print(a.isEmpty())
    a.push(4)
    a.push(5)
    print(a.pop())
    a.print()
    
if __name__ == "__main__":
    main()

