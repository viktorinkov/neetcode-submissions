class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        valid = True
        pos = 0
        while valid:
            if pos < len(strs[0]):
                curr = strs[0][pos] 
            else:
                valid = False
                break
            for word in strs:
                if(pos >= len(word)):
                    valid = False
                    break
                if(word[pos] != curr):
                    valid = False
                    break
            if(valid == False):
                break
            pos += 1
        return strs[0][:pos]
            
        ## bat
        ## bag
        ## bank
        ## band

        