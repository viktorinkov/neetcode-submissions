class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) == 1):
            return 0
        i = 0
        j = 1
        maxProf = 0
        while i < j and j < len(prices) - 1:
            if(prices[i] > prices[j]):
                i += 1
                j += 1
            else:
                curr = prices[j] - prices[i]
                maxProf = max(maxProf, curr)
                j += 1

        while i < j:
                curr = prices[j] - prices[i]
                maxProf = max(maxProf, curr)
                i += 1

        return maxProf