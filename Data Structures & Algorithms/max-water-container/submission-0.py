class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ## we are going to use two pointer method
        ## we are going to create a var to track the maximum amount
        maxAmnt = 0

        ## start at to edges
        l, r = 0, len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r])
            amount = height * (r - l) ## r - l is the width
            if(amount > maxAmnt):
                maxAmnt = amount

            if(heights[l] < heights[r]):
                l += 1
            else:
                r -= 1

        ## Input: height = [1,7,2,5,4,7,3,6]
        ## l = 0; r = 7
        ## iter: 1
        ## amount = 1 * 7
        ## maxAmnt = 7
        ## l = 1; r = 7
        ## iter: 2
        ## amount = 6 * 6 = 36
        ## maxAmnt = 36
        ## l = 1; r = 6
        ## iter: 3
        ## amount = 3 * 5 = 15
        ## maxAmnt = 36
        ## l = 1, r = 5
        ## iter 4
        ## amount = 7 * 4 = 28
        ## maxAmnt = 36
        ## l = 1, r = 4
        ## iter 5
        ## amount = 3 * 4 = 12
        ## maxAmnt = 36
        ## l = 1, r = 3
        ## iter 6 
        ## amoutn = 5 * 2 = 10
        ## maxAmnt = 36
        ## iter 7
        ## l = 1; r = 2
        ## amount = 1 * 2 = 2
        ## maxAmount = 

        return maxAmnt
