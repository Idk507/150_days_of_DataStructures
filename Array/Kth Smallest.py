class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        import heapq
        return heapq.nsmallest(k,arr)[-1]
                
