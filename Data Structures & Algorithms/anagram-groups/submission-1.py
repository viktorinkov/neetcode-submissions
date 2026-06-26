class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time complexity O(n * k)
        # Space complexity O(k)
        mapfirst = {}
        for s in strs:
            map1 = {}
            for char in s:
                map1[char] = map1.get(char, 0) + 1
            key = tuple(sorted(map1.items()))
            if key in mapfirst:
                mapfirst[key].append(s)
            else:
                mapfirst[key] = [s]
        
        return list(mapfirst.values())