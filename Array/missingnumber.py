class Solution:
    def missingNumber(self, arr):
        # code here
        arr.sort()
        res = 1
        for i in range(len(arr)):
            if arr[i] == res :
                res+=1
            elif arr[i] > res :
                break
        return res
