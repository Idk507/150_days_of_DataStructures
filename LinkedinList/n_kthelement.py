'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data   
        self.next = None
'''
        
class Solution:
    def fractional_node(self, head, k):
        # Code here
        count = 0
        curr = head
        
        while curr :
            count +=1
            curr = curr.next
        d = (count // k) if (count % k == 0) else (count // k) + 1        
        pos = 1
        curr = head
        while curr:
            if pos == d :
                return curr.data
            pos+= 1
            curr = curr.next
        return None
        
            
