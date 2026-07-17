class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if(n < 3):
            return 0
        
        l = 0
        r = n - 1

        maxl = height[l]
        maxr = height[r]

        res = 0
        
        while l < r:
            if(maxl < maxr):
                l += 1
                maxl = max(height[l], maxl)
                res += maxl - height[l]
            else:
                r -= 1
                maxr = max(height[r], maxr)
                res += maxr - height[r]
            
        return res
