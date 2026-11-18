"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda i : i.start)
        ends = []
        for interval in intervals:
            if ends and ends[0] <= interval.start:
                heapq.heappop(ends)
            heapq.heappush(ends, interval.end)
        return len(ends)