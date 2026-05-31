class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i, word in enumerate(strs):
            freqs = {}
            for letter in word:
                if(letter in freqs):
                    freqs[letter] += 1
                else:
                    freqs[letter] = 1
            frozen = frozenset(freqs.items())
            if frozen not in res:
                res[frozen] = []
            res[frozen].append(word)
        return list(res.values())
        

                            