class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        for idx in range(len(s) - 1, -1, -1):
            if(s[idx] == "0"):
                dp[idx] = 0
            else:
                dp[idx] = dp[idx+1]

            if(idx + 1 < len(s) and (s[idx] == "1" or s[idx] == "2" and s[idx+1] in "0123456")):
                dp[idx] += dp[idx+2]

        return dp[0]

            