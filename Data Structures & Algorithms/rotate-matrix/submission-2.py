class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        matrix.reverse()
        for i in range(n):
            for j in range(i+1, n):
                matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]