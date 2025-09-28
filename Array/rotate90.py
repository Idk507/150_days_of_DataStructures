class Solution:
    def rotateMatrix(self, mat):
        # code here
        n = len(mat)
        for i in range(n):
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        for j in range(n):
            for i in range(n // 2):
                mat[i][j], mat[n - 1 - i][j] = mat[n - 1 - i][j], mat[i][j]
