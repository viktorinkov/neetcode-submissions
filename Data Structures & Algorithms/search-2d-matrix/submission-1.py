class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # perform bin search on rows
        # then perform bin search on cols

        top_row, bot_row = 0, rows - 1
        while top_row <= bot_row:
            median_row = int((bot_row - top_row) / 2) + top_row
            if(matrix[median_row][0] == target):
                return True
            elif(matrix[median_row][0] < target <= matrix[median_row][-1]):
                top_col, bot_col = 0, cols - 1

                while top_col <= bot_col:
                    median_col = int((bot_col - top_col) / 2) + top_col
                    if(matrix[median_row][median_col] == target):
                        return True
                    elif(matrix[median_row][median_col] > target):
                        bot_col = median_col - 1
                    elif(matrix[median_row][median_col] < target):
                        top_col = median_col + 1
                return False

            elif(matrix[median_row][0] > target):
                bot_row = median_row - 1
            elif(matrix[median_row][0] < target):
                top_row = median_row + 1
            

        return False