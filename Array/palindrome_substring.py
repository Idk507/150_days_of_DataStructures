class Solution:
    def countPS(self, s):
        # code here
        n = len(s)
        count = 0
    
        for center in range(2 * n - 1):
            left = center // 2
            right = left + center % 2
    
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > 1:  # exclude single-character
                    count += 1
                left -= 1
                right += 1
    
        return count

        
