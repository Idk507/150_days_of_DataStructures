'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    #Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
         #code here
        newNode = Node(x)
        if head is None or x <= head.data :
            newNode.next = head
            if head :
                head.prev = newNode
            return newNode 
        
        curr = head
        while curr.next and curr.next.data < x :
            curr = curr.next
        
        if curr.next is None :
            curr.next  = newNode
            newNode.prev = curr
            return head
        
        newNode.next = curr.next
        newNode.prev = curr
        curr.next.prev = newNode
        curr.next = newNode
        return head
    
    
