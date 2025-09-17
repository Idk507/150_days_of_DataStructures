class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr)
        total = N * (N + 1) // 2
        actual = sum(arr)
        return total - actual
