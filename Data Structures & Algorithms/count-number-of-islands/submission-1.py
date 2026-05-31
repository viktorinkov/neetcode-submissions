class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(i, j):
            if(grid[i][j] == "0"):
                return
            visit.add((i, j))
            if(i > 0 and (i-1, j) not in visit):
                bfs(i-1, j)
            if(i < rows - 1 and (i+1, j) not in visit):
                bfs(i+1, j)
            if(j > 0 and (i, j-1) not in visit):
                bfs(i, j-1)
            if(j < cols -1 and (i, j+1) not in visit):
                bfs(i, j + 1)

        for i in range(rows):
            for j in range(cols):
                if((i, j) in visit):
                    continue
                else:
                    if(grid[i][j] == "1"):
                        islands += 1
                        bfs(i, j)

        return islands
