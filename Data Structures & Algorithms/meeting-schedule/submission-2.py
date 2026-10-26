"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.start)
        for idx in range(len(intervals) - 1):
            if intervals[idx + 1].start < intervals[idx].end:
                return False
        return True