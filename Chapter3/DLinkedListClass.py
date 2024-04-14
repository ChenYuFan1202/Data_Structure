#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class DListNode:
    def __init__(self, data = 0):
        self.data = data
        self.left = None
        self.right = None
class DLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0
    def len(self):
        return self._size
    def insert(self, p, value):
        new_node = DListNode(value)
        self._size += 1
        new_node.left = p
        new_node.right = p.right
        p.right.left = new_node#不知道能不能用new_node.right.left
        p.right = new_node
    def append(self, value):
        p = self._head
        new_node = DLinkedList(value)
        self._size += 1
        if p == None:
            self._head = new_node
        else:
            while p.right != None:
                p = p.right
            p.right = new_node
            new_node.left = p
    def delete(self, p):
        p.right.left = p.left
        p.left.right = p.right
        del p
        self._size -= 1
        if self.size == 0:
            self._head = None
    def print(self):
        p = self._head
        while p != None:
            print(p.data, end = " ")
            p = p.right
        print()

        
        
    