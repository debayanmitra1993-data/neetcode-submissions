class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        out = [intervals[0]]

        for idx in range(1, len(intervals)):
            currinterval = intervals[idx]
            previnterval = out[-1]
            if previnterval[1] >= currinterval[0]:
                newinterval = [
                    min(previnterval[0], currinterval[0]),
                    max(previnterval[1], currinterval[1])
                ]
                out.pop()
                out.append(newinterval)
            else:
                out.append(currinterval)
        return out


        
        
        