class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # we have n options to start
        # for each start, we have n - 1 optoins for second
        # for each second we have n - 2 optoins for third
        res = []

        def helper(curr, left):
            if(len(left) == 0):
                res.append(curr)
                return
            for i in range(len(left)):
                new_left = left[:i] + left[i+1:]
                new_curr = curr + [left[i]]
                helper(new_curr, new_left)
        
        helper([], nums)
        return res
        
                