class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ## 9 1 4 2 3 3 7

        ## keep track of what is the longest subsequence if we picked index i
        ## we start with 9
        ## memo[0] = 1
        ## go to one
        ## Is one greater than 9? -> no -> set memo[1] = 1
        ## go to 4
        ## Is four greater than 9 -> no
        ## Is four greater than 1 -> yes -> set memo[2] = 2
        ## go to 2
        ## Is 2 greater than 9 -> no
        ## Is 2 greater than 1 -> yes -> set memo[3] = 2
        ## ...
        ## go to 3
        ## Is 3 greater than 9 -> no
        ## Is 3 greater than 1 -> yes -> set memo[4] = 2
        ## Is 3 greater than 4 -> no
        ## Is 3 greater than 2 -> yes -> set memo[4] = 3
        ## ...
        ## Go to 3
        ## memo[5] = 3
        ## Go to 7
        ## Is 7 greater than 3 -> set memo[6] = 4

        ## basic idea
        ## Use reccurence
        ## memo[i] = max(memo[j] + 1, memo[i]) where j is some index before i s.t. num[j] is < num[i]
        n = len(nums)
        memo = []
        for i in range(n):
            memo.append(1)

        for i in range(1, n):
            for j in range(0, i):
                if(nums[j] < nums[i]):
                    memo[i] = max(memo[j] + 1, memo[i])

        return max(memo)
