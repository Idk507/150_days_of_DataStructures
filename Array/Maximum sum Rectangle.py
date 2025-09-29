class Solution:
    def maxRectSum(self, arr):
        def kadane(arr):
            max_sum = float('-inf')
            curr_sum = 0
            for v in arr:
                curr_sum = max(v, curr_sum + v)
                max_sum = max(max_sum, curr_sum)
            return max_sum

        max_rect_sum = float('-inf')
        row, col = len(arr), len(arr[0])

        for left in range(col):
            temp = [0] * row
            for right in range(left, col):
                for i in range(row):
                    temp[i] += arr[i][right]
                max_rect_sum = max(max_rect_sum, kadane(temp))

        return max_rect_sum
