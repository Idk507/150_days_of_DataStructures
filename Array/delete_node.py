'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        # If the head needs to be removed
        if x == 1:
            return head.next
        
        # Traverse to the node just before the one to be deleted
        current = head
        for i in range(x - 2):
            if current is not None:
                current = current.next
        
        # Delete the x-th node
        if current is not None and current.next is not None:
            current.next = current.next.next
        
        return head
