class Solution:
	def minJumps(self, arr):
	    # code here
	    if arr[0] == 0 : return -1
	    j = 1
	    n = len(arr)
	    maxreach = arr[0]
	    currend = arr[0]
	    for i in range(1,n):
	        maxreach = max(maxreach, arr[i]+i)
	        if i == currend :
	            j += 1
	            currend = maxreach
	            if currend >= n-1:
	                break
	    return j if currend >= n-1 else -1
