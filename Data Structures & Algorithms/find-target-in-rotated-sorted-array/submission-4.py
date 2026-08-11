class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l = 0
        r = n - 1
        # base case: rotated 6 times
        # [1,2,3,4,5,6]
        # [3,4,5,6,1,2]
        # l = 0, m = 2, r = 5, target = 1
        # else -> r = 1

        while l <= r:
            m = (l + r) // 2
            if(nums[m] == target):
                return m
            elif(nums[m] <= nums[r]):
                # m and r are same group
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                    # target is outside m and r
                else:
                    l = m + 1
            else:
                # l and m are same group
                if target < nums[l] or target > nums[m]:
                    # target outside l and m
                    l = m + 1
                else:
                    # target is between l and m
                    r = m - 1
        return -1