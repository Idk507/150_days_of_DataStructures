#User function Template for python3
class Solution:

	def findMaximum(self, arr):
		# code here
		n = len(arr)
		low, high = 0, n - 1
    
        while low <= high:
            mid = low + (high - low) // 2
    
            # Check if mid is the peak
            if (mid == 0 or arr[mid - 1] < arr[mid]) and (mid == n - 1 or arr[mid] > arr[mid + 1]):
                return arr[mid]
            elif mid > 0 and arr[mid - 1] > arr[mid]:
                high = mid - 1  # Move left
            else:
                low = mid + 1   # Move right
    
        return -1  
