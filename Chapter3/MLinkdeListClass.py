#!/usr/bin/env python
# coding: utf-8

# In[2]:


class MListNode:
    def __init__(self, row, col, coef = 1):
        self.row, self.col, self.coef = row, col, coef
        self.right = self.down = None
class MLinkedList:
    def __init__(self, numRow, numCol):
        self.numRow = numRow
        self.numCol = numCol
        self.row = [None] * self.numRow
        self.col = [None] * self.numCol
        self.size = 0

