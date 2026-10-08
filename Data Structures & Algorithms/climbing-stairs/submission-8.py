class Solution:
    def climbStairs(self, n: int) -> int:
        
        # take 1 step
        # take 2 step
        cache = {}
        def dp(i):
            if i < 0:
                return 0
            elif i == 0:
                return 1
            elif i in cache:
                return cache[i]
            cache[i] = dp(i - 1) + dp(i - 2)
            return cache[i]

        return dp(n)
        