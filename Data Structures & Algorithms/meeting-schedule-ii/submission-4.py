"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0 
        intervals.sort(key = lambda x : x.start)
        start_time = intervals[0].start
        end_time = start_time
        for interval in intervals:
            if interval.end > end_time:
                end_time = interval.end
        # print("start_time = ", start_time)
        # print("end_time = ", end_time)

        max_rooms_required = float("-inf") 
        for idx in range(start_time, end_time + 1, 1):
            current_time_in = idx
            current_time_out = idx + 1
            rooms_required = 0
            for meeting in intervals:
                if meeting.start <= current_time_in and meeting.end >= current_time_out:
                    rooms_required += 1
            max_rooms_required = max(max_rooms_required, rooms_required)
            # print("max_rooms_required required for ",current_time_in, " - ", current_time_out, " is ", max_rooms_required)
        return max_rooms_required