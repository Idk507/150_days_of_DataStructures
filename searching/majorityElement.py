class Solution:
    def majorityElement(self, arr):
        #code here
        d= {}
        n = len(arr)
        for i in arr:
            d[i] = d.get(i,0) + 1
            
        for k,v in d.items():
            if v > n // 2 :
                return k
        return -1
                
            
