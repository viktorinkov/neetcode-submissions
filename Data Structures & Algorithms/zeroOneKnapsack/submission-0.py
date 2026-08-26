class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        ROWS = len(weight)
        cache = [[0 for _ in range(capacity + 1)] for _ in range(ROWS)]
    

        for i in range(ROWS):
            for c in range(capacity + 1):
                skip = cache[i-1][c] if i > 0 else 0
                take = 0
                if weight[i] <= c:
                    take = profit[i] + (cache[i - 1][c - weight[i]] if i > 0 else 0)
                cache[i][c] = max(skip, take)
        
        return cache[ROWS-1][capacity]