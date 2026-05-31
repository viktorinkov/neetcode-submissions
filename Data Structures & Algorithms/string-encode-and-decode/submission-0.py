class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            add = str(len(strs[i])) + '#' + strs[i]
            res += add
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        n = len(s)
        result = []
        clutch = False
        lengthAsStr = ""
        lengthAsInt = 0
        i = 0
        while i < n:
            if(clutch == False):
                if(s[i] != '#'):
                    lengthAsStr += s[i]
                else:
                    lengthAsInt = int(lengthAsStr)
                    clutch = True
                    resEntry = ""
                    for j in range(lengthAsInt):
                        resEntry += s[i+j+1]
                    i += lengthAsInt
                    result.append(resEntry)
                    clutch = False
                    lengthAsStr = ""
                    lengthAsInt = 0
                i += 1
        return result
            

            
