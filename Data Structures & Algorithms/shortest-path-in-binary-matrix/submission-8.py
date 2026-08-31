class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        visited = set()
        visited.add((0, 0))
        def bfs(r, c):
            q = deque()
            if(grid[r][c] == 0):
                q.append((r,c, 1))
            else:
                return -1
            while q:
                r, c, l = q.popleft()
                if(r == ROWS-1 and c == COLS - 1):
                    return l

                for dr, dc in directions:
                    new_r = dr + r
                    new_c = dc + c
                    if(min(new_r, new_c) < 0 or new_r == ROWS or new_c == COLS
                    or grid[new_r][new_c] == 1 or (new_r, new_c) in visited):
                        continue
                    # append
                    q.append((new_r, new_c, l + 1))
                    visited.add((new_r, new_c))
            return -1

        return bfs(0, 0)