class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        count = 1
        grpStartIdx = 0
        curGroupChar = chars[0]
        curIndex = 1

        while curIndex < len(chars):
            if(chars[curIndex] == curGroupChar):
                count += 1
                curIndex += 1
            else:
                if(count == 1):
                    curGroupChar = chars[curIndex]
                    grpStartIdx = curIndex
                    curIndex += 1
                    continue
                else:
                    countAsString = str(count)
                    removeLen = curIndex - grpStartIdx - len(countAsString)
                    # a, b, b, b, b, c
                    # grpStartIdx = 1
                    # curIndex = 5
                    # removeLen = 5- 1 - 1 = 3
                    # remove elemnts 2 to 1 + 3 - 1 = 3 inclusive
                    for i in range(removeLen - 1):
                        del chars[grpStartIdx + 1]
                    # add countAsString
                    j = 0
                    for i in range(grpStartIdx + 1, grpStartIdx + len(countAsString) + 1):
                        chars[i] = countAsString[j]
                        j += 1
                    # continue
                    curIndex -= (removeLen - len(countAsString))
                    curGroupChar = chars[curIndex]
                    grpStartIdx = curIndex
                    curIndex += 1
                    count = 1
                    
        if(count != 1):
            countAsString = str(count)
            removeLen = curIndex - grpStartIdx - len(countAsString)
            for i in range(removeLen - 1):
                del chars[grpStartIdx + 1]
            j = 0
            for i in range(grpStartIdx + 1, grpStartIdx + len(countAsString) + 1):
                chars[i] = countAsString[j]
                j += 1


        return len(chars)
