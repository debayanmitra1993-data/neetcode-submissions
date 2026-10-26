class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x : x[0])

        mystack = []
        mystack.append(intervals.pop())

        while len(intervals) > 0:

            ele = intervals.pop()

            while len(mystack) > 0:
                if ele[1] >= mystack[-1][0]:
                    popped_ele = mystack.pop()
                    ele = [ele[0], max(ele[1], popped_ele[1])]
                else:
                    break
            mystack.append(ele)
        return mystack[::-1]
        