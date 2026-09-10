class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[-1 for _ in range(n)] for _ in range(m)]

        for row in range(m):
            for col in range(n):
                prev = 1 if row == 0 and col == 0 else 0
                if(row != 0):
                    prev += cache[row-1][col]
                if(col != 0):
                    prev += cache[row][col-1]

                cache[row][col] = prev

        return cache[m-1][n-1]