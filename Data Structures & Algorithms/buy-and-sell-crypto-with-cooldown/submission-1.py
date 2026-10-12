class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0

        holding = -prices[0]
        notHolding = 0
        prevNotHolding = 0      
        
        for i in range(1, n):
            # cache[True][i] = max((cache[False][i-2] if i >= 2 else 0) - prices[i], cache[True][i-1])
            newHolding = max(prevNotHolding - prices[i], holding)
            newNotHolding = max(notHolding, holding + prices[i])

            prevNotHolding = notHolding
            holding = newHolding
            notHolding = newNotHolding


            # not holding: max of do nothing or sell
            # cache[False][i] = max(cache[False][i-1], cache[True][i-1] + prices[i])

        
        return notHolding