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
        for idx in range(1, len(intervals)):
            current_interval = intervals[idx]
            prev_interval = intervals[idx - 1]

            if current_interval.start < prev_interval.end:
                return False 
        return True 