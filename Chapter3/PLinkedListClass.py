#!/usr/bin/env python
# coding: utf-8

# In[1]:


class PListNode:
    def __init__(self, coef = 1, expo = 0):
        self.coef = coef
        self.expo = expo
        self.next = None
class PLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0
    def insert(self, p, co, ex):
        new_node = PListNode(co, ex)
        if self._head is None:
            self._head = new_node
        else:
            new_node.next = p.next
            p.next = new_node
        return new_node
    def print(self):
        p = self._head
        while p.next:
            print(f"{p.coef}x^{p.expo} + ", end = "")
            p = p.next
        print(f"{p.coef}x^{p.expo}")

