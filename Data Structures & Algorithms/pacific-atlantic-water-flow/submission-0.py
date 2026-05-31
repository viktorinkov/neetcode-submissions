class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ## given heights of different points
        ## <- -> ^ \/ directions allowed
        ## no diag movement
        ## only move from high to eq/low
        ## find all that lead to both (top or left) and (down or right)

        ## basic observations
        ## top right and bottom left are always solutions

        ## heights is a 2d matrix
        
        ## A brute force
        ## go through each cell
        ## for each cell, run bfs with travel restrictions
        ## basically each cell is a node whose neighbours are lower or equal in value

        ## we notice that all pacific nodes are top left and all atlantic nodes are bottom right
        ## we can traverse in reverse

        pacific = []
        atlantic = []

        rows, cols = len(heights), len(heights[0])

        def local_check_pacific(r, c):
            if(c > 0):
                ## left check
                if([r, c-1] not in pacific and heights[r][c-1] >= heights[r][c]):
                    pacific.append([r, c-1])
                    local_check_pacific(r, c-1)
            if(r > 0):
                ## top check
                if([r-1, c] not in pacific and heights[r-1][c] >= heights[r][c]):
                    pacific.append([r-1, c])
                    local_check_pacific(r-1, c)
            if(r < rows-1):
                ## bottom check
                if([r+1, c] not in pacific and heights[r+1][c] >= heights[r][c]):
                    pacific.append([r+1, c])
                    local_check_pacific(r+1, c)
            if(c < cols-1):
                ## right check
                if([r, c+1] not in pacific and heights[r][c+1] >= heights[r][c]):
                    pacific.append([r, c+1])
                    local_check_pacific(r, c+1)

        
        def local_check_atlantic(r, c):
            if(c > 0):
                ## left check
                if([r, c-1] not in pacific and heights[r][c-1] >= heights[r][c]):
                    atlantic.append([r, c-1])
                    local_check_atlantic(r, c-1)
            if(r > 0):
                ## top check
                if([r-1, c] not in atlantic and heights[r-1][c] >= heights[r][c]):
                    atlantic.append([r-1, c])
                    local_check_atlantic(r-1, c)
            if(r < rows-1):
                ## bottom check
                if([r+1, c] not in atlantic and heights[r+1][c] >= heights[r][c]):
                    atlantic.append([r+1, c])
                    local_check_atlantic(r+1, c)
            if(c < cols-1):
                ## right check
                if([r, c+1] not in atlantic and heights[r][c+1] >= heights[r][c]):
                    atlantic.append([r, c+1])
                    local_check_atlantic(r, c+1)

        ## append all top and left to pacfic
        for c in range(cols):
            pacific.append([0, c])
            local_check_pacific(0, c)

        for r in range(rows):
            pacific.append([r, 0])
            local_check_pacific(r, 0)
        
        ## append all bottom and right to atlantic
        for c in range(cols):
            atlantic.append([rows-1, c])
            local_check_atlantic(rows-1, c)
        
        for r in range(rows):
            atlantic.append([r, cols-1])
            local_check_atlantic(r, cols-1)

        result = []
        ## check which points belong to both categories
        for r in range(rows):
            for c in range(cols):
                if([r, c] in atlantic and [r,c] in pacific):
                    result.append([r, c])

        return result

        
