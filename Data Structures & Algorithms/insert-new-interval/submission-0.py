class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x : x[0])

        idx = 0
        while True:
            merged = False
            if idx + 1 <= len(intervals) - 1:
                first_interval = intervals[idx]
                second_interval = intervals[idx + 1]
                if first_interval[1] >= second_interval[0]:
                    new_interval = [first_interval[0], max(first_interval[1], second_interval[1])]
                    intervals[idx] = new_interval
                    intervals.pop(idx + 1)
                    merged = True
                else:
                    idx += 1
            else:
                break
        return intervals
            




        