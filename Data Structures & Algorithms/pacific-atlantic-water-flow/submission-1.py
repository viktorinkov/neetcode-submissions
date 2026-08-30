class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # all pacific borders
        # all atlantic borders
        pacific = set()
        atlantic = set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visit, prevHeight):
            if(min(r,c) < 0 or r == ROWS or c == COLS
                or (r, c) in visit or heights[r][c] < prevHeight):
                return
            
            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        res = []
        for a_pair in atlantic:
            for p_pair in pacific:
                if(a_pair == p_pair):
                    res.append(a_pair)
        
        return res