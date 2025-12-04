class Solution:
    def search(self, arr, x):
        # code here
        n = len(arr)
        # l,h = 0,n-1
        
        # while l <= h :
        #     m = (l+h) //2 
        #     if arr[m] == x :
        #         return m
        #     elif arr[m] <= x:
        #         l = m+1
        #     else :
        #         r = m-1
        # return -1
        for i in range(n):
            if arr[i] == x : 
                return i
        return -1
