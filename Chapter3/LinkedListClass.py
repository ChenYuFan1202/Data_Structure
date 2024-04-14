#!/usr/bin/env python
# coding: utf-8

# In[11]:


class LinkNode:
    def __init__(self, data = 0):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self._head = None#_代表約定成俗的私有屬性
        self._size = 0
    def len(self):
        return self._size
    def append(self, value):
        p = self._head
        new_node = LinkNode(value)
        self._size += 1
        if p == None:
            self._head = new_node
            return
        while p.next != None:
            p = p.next
        p.next = new_node
    def find(self, value):
        p = self._head
        while p != None:
            if p.data == value:
                return p
            p = p.next
        return None
    def insertAfter(self, p, value):
        new_node = LinkNode(value)
        self._size += 1
        if p == None:
            new_node.next = self._head
            self._head = new_node
            return 
        new_node.next = p.next
        p.next = new_node
    def delete(self, value):
        old_node = self._head
        pre_node = None
        while old_node != None:
            if old_node.data == value:#沒有.data的話是指標
                break
            pre_node = old_node
            old_node = old_node.next
        if old_node != None:
            if pre_node == None:
                self._head = old_node.next
            else:
                pre_node.next = old_node.next
            del old_node#上面不管是哪個，都會del old_node
        #return 有沒有寫都可以
    def print(self):
        p = self._head
        while p != None:
            print(p.data, end = " ")
            p = p.next
        print()
        
    def reverse(self):
        if self._size < 2:
            return 
        p = self._head
        q = p.next
        r = q.next
        p.next = None
        while q: # q != None
            q.next = p
            p = q
            q = r
            if r:
                r = r.next
        self._head = p
        
    def reverse2(self, p, q, r):
        if r is None:
            q.next = p
            self._head = q
        else:
            self.reverse2(q, r, r.next)
            q.next = p
        
        
def main():
    a = LinkedList()
    a.insertAfter(None, 99)#return沒有print不會有None
    a.append(4)
    a.append(1)
    p = a.find(4)
    a.insertAfter(p, 444)
    a.append(8)
    a.append(5)
    a.append(4)
    a.print()
    a.delete(99)
    a.print()
    
    
if __name__ == "__main__":
    main()
