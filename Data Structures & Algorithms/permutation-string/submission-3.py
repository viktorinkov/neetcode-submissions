class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = {}
        for char in s1:
            s1map[char] = s1map.get(char, 0) + 1
        
        l = 0
        
        # abc
        # dbca
        s2antimap = s1map.copy()
        for r in range(len(s2)):
            if(s2[r] not in s1map):
                s2antimap = s1map.copy()
                l = r + 1
                continue
            # normal case
            s2antimap[s2[r]] -= 1
            while(s2antimap[s2[r]] < 0):
                s2antimap[s2[l]] += 1
                l += 1
                continue
            extras = sum(s2antimap.values())
            if(extras == 0):
                return True

        return False



       # abc
       # lecabee
       # l
       # l = r = 0
       # l = r = 1
       # l = r = 2
       # no extras
       # l = 2; r = 3
       # l = 2; r =4
            