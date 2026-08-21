class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # run bfs from each rotten fruit
        q = deque()
        mins = 0
        def bfs():
            nonlocal mins
            nonlocal q
            visited = set()
            while q:
                rotted = False
                for _ in range(len(q)):
                    curr = q.popleft()
                    x, y = curr
                    if(grid[x][y] == 0 or (x,y) in visited):
                        continue
                    
                    if grid[x][y] == 1:
                        rotted = True
                    grid[x][y] = 2
                    visited.add((x,y))

                    if(x > 0):
                        q.append((x-1, y))
                    if(x < len(grid) - 1):
                        q.append((x+1, y))
                    if(y > 0):
                        q.append((x, y - 1))
                    if(y < len(grid[0]) - 1):
                        q.append((x, y + 1))
                if rotted:
                    mins += 1
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == 2):
                    q.append((row,col))
        bfs()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == 1):
                    return -1
        return mins