class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0

        map1 = {}
        for char in t:
            map1[char] = map1.get(char, 0) + 1

        map2 = {}
        needs = sum(map1.values())
        winPairs = []
        for r in range(len(s)):
            if(s[r] in map1):
                map2[s[r]] = map2.get(s[r], 0) + 1
                #
                if(map2[s[r]] <= map1[s[r]]):
                    needs -= 1
            
            # case we no longer have needs
            while(needs == 0):
                winPairs.append((l, r))
                # start looping to increase l
                
                # remove l
                if(s[l] in map1):
                    map2[s[l]] = map2[s[l]] - 1
                    if(map2[s[l]] < map1[s[l]]):
                        needs += 1

                l += 1
        print(winPairs)
        if(winPairs == []):
            return ""
        else:
            shortest = winPairs[0]
            for pair in winPairs:
                curr = pair[1] - pair[0] + 1
                shortestVal = shortest[1] - shortest[0] + 1
                if(shortestVal > curr):
                    shortest = pair
        start = shortest[0]
        end = shortest[1]
        return s[start:(end+1)]

            
