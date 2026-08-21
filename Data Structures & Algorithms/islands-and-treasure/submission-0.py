class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        def bfs():    
            nonlocal q        
            visited = set()
            distance = 0
            while q:
                for _ in range(len(q)):
                    # check each neighbor
                    curr = q.popleft()
                    c_x, c_y = curr
                    if(curr in visited):
                        continue
                    else:
                        visited.add(curr)
                    
                    if(grid[c_x][c_y] == -1):
                        continue
                    
                    # check all curr neighbours and add them to q
                    # for each nei, we need to update their closeness
                    
                    grid[c_x][c_y] = min(distance, grid[c_x][c_y])
                    if(c_x > 0):
                        q.append((c_x - 1, c_y))
                    if(c_x < len(grid) - 1):
                        q.append((c_x + 1, c_y))
                    if(c_y > 0):
                        q.append((c_x, c_y - 1))
                    if(c_y < len(grid[0]) - 1):
                        q.append((c_x, c_y + 1))
                distance += 1
                
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == 0):
                    q.append((row,col))
        bfs()