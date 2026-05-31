class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        output = []

        ## [0, 0], [0, 1], [0, 2]
        ## [0, 2], [1, 2], [2, 2]
        ## [2, 2], [2, 1], [2, 0]
        ## [2, 0], [1, 0]
        ## [1, 1]


        ## 1 2 3 5 
        ## 6 7 8 9
        ## 10 11 12 13

        ## [0, 0], [0, 1], [0, 2], [0, 3]
        ## [1, 3], [2, 3]
        ## [2, 2,], [2, 1], [2, 0]
        ## [1, 0], [1, 1], [ 1, 2], [1, 2]
        top = 0
        left = 0
        right = cols - 1
        bot = rows - 1
        horLim = cols / 2
        verLim = rows / 2
        cur = [top, left]
        direction = [0, 1]
        while top <= bot and left <= right:
            ## once we reach top right, we increase top
            while direction == [0, 1]:
                output.append(matrix[cur[0]][cur[1]])
                if(cur == [top, right]):
                    top += 1
                    direction = [1, 0]
                    cur = [cur[0] + 1, cur[1]]
                else:
                    cur = [cur[0], cur[1] + 1]
            ## once we reach bottom right, we reduce right
            while direction == [1, 0] and top <= bot:
                output.append(matrix[cur[0]][cur[1]])
                if(cur == [bot, right]):
                    right -= 1
                    direction = [0, -1]
                    cur = [cur[0], cur[1] - 1]
                else:
                    cur = [cur[0] + 1, cur[1]]
            ## once we reach bottom left, we reduce bottom
            while direction == [0, -1]  and left <= right:
                output.append(matrix[cur[0]][cur[1]])
                if(cur == [bot, left]):
                    bot -= 1
                    direction = [-1, 0]
                    cur = [cur[0] - 1, cur[1]]
                else:
                    cur = [cur[0], cur[1] - 1]
            ## once we reach top left, we increase left
            while direction == [-1, 0] and top <= bot:
                output.append(matrix[cur[0]][cur[1]])
                if(cur == [top, left]):
                    left += 1
                    direction = [0, 1]
                    cur = [cur[0], cur[1] + 1]
                else:
                    cur = [cur[0] - 1, cur[1]]
        return output
