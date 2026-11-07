class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        steps = 0
        while r < n - 1:
            reach = 0
            for i in range(l, r + 1):
                reach = max(reach, i + nums[i])
            l = r + 1
            r = reach
            steps += 1
        return steps
        