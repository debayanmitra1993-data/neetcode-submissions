"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        hour_points = {}
        for interval in intervals:
            if interval.start not in hour_points:
                hour_points[interval.start] = True
            if interval.end not in hour_points:
                hour_points[interval.end] = True
        
        hour_points = list(hour_points.keys())
        hour_points.sort()

        maxstore = 0
        for idx in range(len(hour_points) - 1):
            start_hr = hour_points[idx]
            end_hr = hour_points[idx + 1]
            cnt = 0
            for interval in intervals:
                if interval.start <= start_hr and interval.end >= end_hr:
                    cnt += 1
            if cnt > maxstore:
                maxstore = cnt
        return maxstore


        