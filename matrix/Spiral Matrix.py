"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix : return []
        rows,cols = len(matrix),len(matrix[0])
        top,bottom,left,right = 0,rows-1,0,cols-1
        outputs = []

        while len(outputs) < rows * cols :
            for i in range(left,right+1):
                outputs.append(matrix[top][i])
            top += 1 

            for i in range(top,bottom+1):
                outputs.append(matrix[i][right])
            right -=1

            if top <= bottom :
                for i in range(right, left-1, -1):
                    outputs.append(matrix[bottom][i])
                bottom -=1
            if left <= right:
                for i in range(bottom,top-1,-1):
                    outputs.append(matrix[i][left])
                left+=1
        return outputs        
