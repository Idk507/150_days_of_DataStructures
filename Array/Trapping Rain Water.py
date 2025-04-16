"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxl = [0]*n
        maxr = [0]*n

        maxl[0]=height[0]
        maxr[n-1] = height[n-1]
        for i in range(1,len(height)):
            maxl[i] = max(maxl[i-1],height[i])
        for j in range(n-2,-1,-1):
            maxr[j] = max(maxr[j+1],height[j])

        tap = 0
        for i in range(n):
            tap+= min(maxl[i],maxr[i]) - height[i]
        return tap
