class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cache = [[False for _ in range(n)] for _ in range(n)]
        res = 0

        def dp(i, j):
            nonlocal res
            if(i == j or (s[i] == s[j] and (j - i == 1 or cache[i + 1][j - 1] == True))):
                cache[i][j] = True
            if cache[i][j]:
                res += 1
            return cache[i][j]
        
        for j in range(n):
            for i in range(j + 1):
                dp(i, j)
        return res
                