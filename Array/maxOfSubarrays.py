class Solution:
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        res = []
        if k == 1:
            return arr
        
        for i in range(n - k + 1):  
            m = arr[i]
            for j in range(i, i + k):
                m = max(m, arr[j])
            res.append(m)
        
        return res
