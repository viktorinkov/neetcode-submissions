"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        index1 = 0
        index2 = 0
        count = 0
        maxCount = 0
        n = len(start)
        while index1 < n:
            if(start[index1] < end[index2]):
                index1 += 1
                count += 1
            else:
                index2 += 1
                count -= 1
            if(count > maxCount):
                maxCount = count
        
        return maxCount
