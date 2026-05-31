class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        ## 12
        ## - 10 or -5 or -1

        ## memory optimized variant

        memo = {}
        ## key is amount
        ## value is coins used
        
        ## main idea
        ## top down
        ## for each amount smaller than our target value
        ## remove each coin denom from total amount
        
        def dfs(cur):
            if(cur == 0):
                return 0
            if cur in memo:
                return memo[cur]

            count = 1e9
            for denum in coins:
                if(cur - denum >= 0):
                    count = min(count, 1 + dfs(cur - denum))
                
            memo[cur] = count
            return count
        
        res = dfs(amount)
        return -1 if res >= 1e9 else res
            
            

