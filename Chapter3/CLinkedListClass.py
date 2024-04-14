#!/usr/bin/env python
# coding: utf-8

# In[2]:


class ListNode:
    def __init__(self, data = 0):
        self.data = data
        self.next = None
class CLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0
    def len(self):
        return self._size
    def append(self, value):
        p = self._head
        new_node = ListNode(value)
        self._size += 1
        if p is None:
            self._head = new_node
        else:
            while p.next != self._head:#也就是不等於最後一個的時候
                p = p.next
            p.next = new_node#改變原來最後節點的指標
        new_node.next = self._head#無論如何，會將最後一個指向第一個節點
    def find(self, value):
        if self._size == 0:
            return
        p = self._head
        while p.next != self._head:#不是最後一個的時候
            if p.data == value:
                return p
            p = p.next
        if p.data == value:    #比較最後一個節點 
            return p
        return None
    def print(self):
        if self._size == 0:
            return
        p = self._head
        while p.next != self._head:
            print(p.data, end = " ")
            p = p.next
        print(p.data)#最後一個節點的資料
        
def main():
    a = CLinkedList()
    a.append(4)
    a.append(8)
    a.append(1)
    a.append(5)
    a.append(4)
    a.print()
    
if __name__ == "__main__":
    main()

