class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        n = len(cost)
        def dp(idx):
            if (idx == 0 or idx == 1):
                return cost[idx]
            elif idx in cache:
                return cache[idx]
            elif idx == n:
                cache[idx] = min(dp(idx-1), dp(idx-2))
            else: 
                cache[idx] = min(dp(idx-1), dp(idx-2)) + cost[idx]
            return cache[idx]
        
        return dp(len(cost))