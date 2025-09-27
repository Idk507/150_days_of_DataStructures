class Solution:
    def transpose(self, mat):
        # code here
        r ,c = len(mat), len(mat[0])
        tra = [[0]*r  for i in range(c)]
        for i in range(r):
            for j in range(c):
                tra[j][i] = mat[i][j]
        return tra
            
