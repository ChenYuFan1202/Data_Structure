#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Queue:
    def __init__(self):
        self.item = list()
    def isEmpty(self):
        return len(self.item) == 0
    def isFull(self):
        return False

    def enQueue(self, value):
        if not self.isFull():
            self.item.append(value)
    def deQueue(self):
        if not self.isEmpty():
            return self.item.pop(0)
        return None
    def peekFront(self):
        if not self.isEmpty():
            return self.item[0]
        return None
    def peekRear(self):
        if not self.isEmpty():
            return self.item[-1]
        return None
    def print(self):
        for i in range(len(self.item)):
            print(self.item[i], end = " ")
        print()
        
def main():
    a = Queue()
    print(a.isEmpty())
    a.enQueue(4)
    a.enQueue(5)
    a.enQueue(6)
    print(a.deQueue())
    a.print()
        
if __name__ == "__main__":
    main()

