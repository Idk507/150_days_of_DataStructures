class Solution:

    def heapSort(self, arr):
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
        
            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right
        
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]  # swap
                heapify(arr, n, largest)
        def buildHeap(arr, n):
            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)
        n = len(arr)        
        buildHeap(arr, n)

        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]  # Swap root with last
            heapify(arr, i, 0) 
            
