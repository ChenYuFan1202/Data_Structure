#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Stack:
    def __init__(self):
        self.item = list()
    def isEmpty(self):
        return len(self.item) == 0
    def isFull(self):
        return False#有設最大值(MAX_ITEM)的話，return len(self.item) >= MAX_ITEM
    def push(self, value):
        if not self.isFull():
            self.item.append(value)
    def pop(self):
        if not self.isEmpty():
            return self.item.pop()
        else:
            return None
    def peek(self):
        if not self.isEmpty():
            return self.item[-1]
    def print(self):
        print("top to bottom: ", end = "")
        for i in range(1 , len(self.item) + 1):
            print(self.item[-i], end = " ")
        print()
        
def main():
    a = Stack()
    print(a.isEmpty())
    a.push(4)
    a.push(5)
    print(a.pop())
    a.push(6)
    print(a.peek())
    a.print()
        
if __name__ == "__main__":
    main()

