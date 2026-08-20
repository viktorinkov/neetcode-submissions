class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            nonlocal grid
            # mark current as visited
            if(grid[x][y] == "0"):
                return
            
            grid[x][y] = "0"

            # visit all non-zero's
            if(x > 0):
                dfs(x - 1, y)
            if(x < len(grid) - 1):
                dfs(x + 1, y)
            if(y > 0):
                dfs(x, y - 1)
            if(y < len(grid[0]) - 1):
                dfs(x, y + 1)
        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if(grid[x][y] == "1"):
                    res += 1
                    dfs(x, y)
        
        return res
