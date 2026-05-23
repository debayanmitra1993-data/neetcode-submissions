class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        print("intervals = ", intervals)
        merged_intervals = [intervals[0]]
        idx = 1
        while idx < len(intervals):
            curr_interval = intervals[idx]
            prev_interval = merged_intervals[-1]
            if curr_interval[0] <= prev_interval[1]:
                merged_intervals.pop()
                merged_intervals.append([
                    min(prev_interval[0], curr_interval[0]), 
                    max(prev_interval[1], curr_interval[1])
                ])
            else:
                merged_intervals.append(curr_interval)
            idx += 1
        return merged_intervals

        