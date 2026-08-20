class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        curr = 0
        def dfs(x, y):
            nonlocal curr
            nonlocal grid
            if(grid[x][y] == 0):
                return
            
            grid[x][y] = 0
            curr += 1
            if(x > 0):
                dfs(x - 1, y)
            if(x < len(grid) - 1):
                dfs(x + 1, y)
            if(y > 0):
                dfs(x, y - 1)
            if(y < len(grid[0]) - 1):
                dfs(x, y + 1)

        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if(grid[x][y] == 1):
                    curr = 0
                    dfs(x, y)
                    res = max(curr, res)
                else:
                    curr = 0
        
        return res