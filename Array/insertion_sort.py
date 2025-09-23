class Solution:
    def insertionSort(self, arr):
        # code here
        n = len(arr)
        for i in range(n):
            k = arr[i]
            j = i - 1
            while j>=0 and arr[j] > k :
                arr[j+1] = arr[j]
                j-= 1
            arr[j+1] = k
        return arr
