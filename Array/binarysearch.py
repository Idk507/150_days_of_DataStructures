#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        #Your code here
        n = len(arr)
        l,h = 0, n-1
        while (l <= h):
            m = (l+h)//2
            if arr[m] == k :
                return True
            elif arr[m] < k:
                l+=1
            else :
                r-=1
        return False
