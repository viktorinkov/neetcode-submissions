class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) <= 1):
            return 0
        maxProfit = 0
        l = 0
        r = 1

        while r < len(prices):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                if(diff > maxProfit):
                    maxProfit = diff
            else:
                l = r
            r += 1
             
            
        ## 10, 1, 5, 6, 7, 1
        ## l = 0
        ## r = 1
        ## iter 1
        ## diff = 1 - 10 = -9
        ## l = 0, r = 2
        ## iter 2
        ## diff = 5 - 10 = -5
        ## l = 

        return maxProfit

