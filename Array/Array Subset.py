#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        from collections import Counter 
        count_a = Counter(a)
        count_b = Counter(b)
        for e in count_b :
            if count_b[e] > count_a.get(e,0) :
                return False
        return True
        
            
            
            
    
    
    
