class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
        
            m = (l+r) // 2
            if(nums[m] == target):
                return m

            if(nums[l] <= nums[m]): ## i.e. it means m is a part of the left seq
                if(target > nums[m]):
                    l = m + 1
                elif target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else: ## i.e. m is part of the right sequence
                if(target < nums[m]):
                    r = m-1
                elif(target > nums[r]):
                    r = m-1
                else:
                    l = m + 1

        ## [3,4,5,6,1,2] target = 1
        ## l = 0, r = 5
        ## m = 2
        ## 

        return -1
