class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        n = len(nums)
        longest = 0
        curr = 0
        for num in nums:
            # check if start of seq
            if( (num - 1) not in myset):
                while( (num + curr) in myset):
                    curr += 1
                if(curr > longest):
                    longest = curr
                curr = 0
        return longest


