class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        myMap = {}
        def dp(local_s):
            if local_s == "":
            # loop all possible words
                myMap[local_s] = True
                return True
            elif local_s in myMap:
                return myMap[local_s]
            res = False
            for word in wordSet:
                if len(word) > len(local_s):
                    continue
                
                if local_s[:len(word)] == word:
                    if dp(local_s[len(word):]):
                        myMap[local_s] = True
                        return True

            myMap[local_s] = False
            return False
        
        return dp(s)

