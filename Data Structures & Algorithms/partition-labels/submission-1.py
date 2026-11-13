class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ends = {}
        for i in range(len(s) - 1, - 1, -1):
            if s[i] not in ends:
                ends[s[i]] = i
        res = []
        minCut = 0
        minStart = 0

        for i in range(len(s)):
            minCut = max(ends[s[i]], minCut)

            if minCut == i:
                res.append(i - minStart + 1)
                minStart = i + 1
        
        return res
                