class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)
        n = len(text2)
        cache = [[0 for _ in range(n)] for _ in range(m)]
        def dp(i1, i2):
            if(i1 < 0 or i2 < 0):
                return 0
            if(cache[i1][i2] != 0):
                return cache[i1][i2]
            if(text1[i1] == text2[i2]):
                cache[i1][i2] = dp(i1-1, i2-1) + 1
            else:
                cache[i1][i2] = max(dp(i1 - 1, i2), dp(i1, i2 - 1)) 
            
            return cache[i1][i2]

        return dp(m - 1, n - 1)