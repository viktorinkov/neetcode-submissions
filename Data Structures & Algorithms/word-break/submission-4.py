class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        shrtsValidLen = 1e9
        for word in wordDict:
            if(len(word) < shrtsValidLen):
                shrtsValidLen = len(word)

        def dfs(target):
            if(target == ""):
                return True
            if(len(target) < shrtsValidLen):
                return False
            if(target in dp):
                return dp[target]
            else:
                for word in wordDict:
                    ## remove word substring from s
                    if(target.startswith(word)):
                        temp = target[len(word):]
                        if(dfs(temp) == True):
                            dp[target] = True
                            return True
            dp[target] = False
            return False
        ## neetcode
        ## 
        return dfs(s)