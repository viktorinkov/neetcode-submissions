class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        tMap = {}
        for char in t:
            if char in tMap:
                tMap[char] += 1
            else:
                tMap[char] = 1

        window = {}
        for key in tMap.keys():
            window[key] = 0
        
        need = 0
        have = 0
        for key, val in tMap.items():
            need += val
        
        bestLen = float('inf')
        bestStart = 0
        start = 0
        end = 0
        
        while end < len(s):
            endChar = s[end]
            if(endChar in tMap.keys()):
                window[endChar] += 1
                if(window[endChar] <= tMap[endChar]):
                    have += 1
            
            while(need == have):
                ## check for best
                currLen = end - start + 1
                if(currLen < bestLen):
                    bestStart = start
                    bestLen = currLen
                # Update window when shrinking
                startChar = s[start]
                if startChar in tMap:
                    window[startChar] -= 1
                    if window[startChar] < tMap[startChar]:
                        have -= 1
                start += 1
            
            end += 1
        
        if(bestLen < float('inf')):
            endIndex = bestStart + bestLen
            return s[bestStart:endIndex]
        else:
            return ""