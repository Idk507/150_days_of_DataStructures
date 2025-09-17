class Solution:
    def missingNum(self, arr):
        # code here
        N = max(arr)
        total = N * (N + 1) // 2
        actual = sum(arr)
        return total - actual
