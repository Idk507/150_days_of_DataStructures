#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        j = 0
        curr = 0
        for i in range(len(arr)):
            curr += arr[i]
            
             
            while curr > target and j < i :
                curr-=arr[j]
                j+=1
            if curr == target : return[j+1,i+1]
        return [-1]
