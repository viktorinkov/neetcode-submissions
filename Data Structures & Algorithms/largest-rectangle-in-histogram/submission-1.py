class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        maxArea = 0
        stack = [] # position, height

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index)) 
                # do not need to add one since we are not counting the current i (i-1) - index + 1 is what we are doing for width
                start = index

            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea