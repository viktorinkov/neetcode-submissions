class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals =sorted(intervals, key=lambda item: item[0] )
        res = [intervals[0]]
        for start, end in intervals:
            prevEnd = res[-1][1]
            if(prevEnd >= start):
                res[-1][1] = max(end, prevEnd)
            else:
                res.append([start,end])

        ## [[1,3],[1,5],[6,7]]

        return res
