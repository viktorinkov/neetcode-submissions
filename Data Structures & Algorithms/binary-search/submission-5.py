class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(len(nums) == 1):
            return 0 if nums[0] == target else -1
        
        low = 0
        high = len(nums)-1
        mid = (low+high) // 2

        while low <= high:
            if(target == nums[mid]):
                return mid
            if(target < nums[mid]):
                high = mid - 1
                mid = (low+high) // 2
            if(target > nums[mid]):
                low = mid + 1
                mid = (low+high) // 2

        return -1
