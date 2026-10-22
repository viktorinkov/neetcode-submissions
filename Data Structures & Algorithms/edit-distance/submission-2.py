class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        cache = [[-1 for _ in range(m)] for _ in range(n)]

        def dp(i, j):
            if i == n:
                return m - j
            if j == m:
                return n - i
            if cache[i][j] != -1:
                return cache[i][j]
            if word1[i] == word2[j]:
                cache[i][j] = dp(i+1, j+1)
            else:
                # replace
                # delete
                # exchange
                insertCost = dp(i + 1, j) + 1
                deleteCost = dp(i, j+1) + 1
                exchangeCost = dp(i+1, j+1) + 1
                cache[i][j] = min(insertCost, deleteCost, exchangeCost)
            return cache[i][j]
        
        return dp(0, 0)
