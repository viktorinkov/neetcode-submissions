class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for interval in intervals:
            if interval[0] <= newInterval[0] <= interval[1]:
                newInterval[0] = interval[0]
            if interval[0] <= newInterval[1] <= interval[1]:
                newInterval[1] = interval[1]
        i = 0
        added = False
        while i < len(intervals):
            if added:
                if intervals[i][1] <= newInterval[1]:
                    intervals.pop(i)
                    continue
            elif intervals[i][0] >= newInterval[0]:
                intervals.insert(i, newInterval)
                added = True

            i += 1

        if not added:
            intervals.append(newInterval)
        
        return intervals
