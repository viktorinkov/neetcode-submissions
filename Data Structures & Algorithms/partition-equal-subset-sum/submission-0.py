class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for num in nums:
            total += num
        if(total % 2 != 0):
            return False
        
        target = total // 2
        # now we want to find 2 subsets such that they both equal target

        cache = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]

        for i in range(len(nums) + 1):
            cache[i][0] = True

        for n in range(len(nums) + 1):
            for c in range(1, target + 1):
                # get "or" of include or not
                res = cache[n-1][c] if n > 0 else False

                if n > 0 and c - nums[n - 1] >= 0:
                    res = res or cache[n - 1][c - nums[n - 1]]
                cache[n][c] = res

        return cache[len(nums)][target]