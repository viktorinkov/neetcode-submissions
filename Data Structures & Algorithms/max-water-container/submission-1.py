class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        mymax = 0
        while l < r:
            h = min(heights[l], heights[r])
            w = r - l
            cur = w * h
            mymax = max(mymax, cur)
            if(heights[r] > heights[l]):
                l += 1
            else:
                r -= 1
        
        return mymax