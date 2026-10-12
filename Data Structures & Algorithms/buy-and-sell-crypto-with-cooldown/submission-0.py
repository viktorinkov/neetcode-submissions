class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cache = [[0 for _ in range(n)] for _ in [True, False]]

        # holding
        cache[True][0] = -prices[0]
        for i in range(1, n):
            # holding: max of buy or do nothing
            cache[True][i] = max((cache[False][i-2] if i >= 2 else 0) - prices[i], cache[True][i-1])

            # not holding: max of do nothing or sell
            cache[False][i] = max(cache[False][i-1], cache[True][i-1] + prices[i])
        
        return cache[False][n-1]