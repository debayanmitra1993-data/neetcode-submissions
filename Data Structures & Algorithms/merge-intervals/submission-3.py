class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        mystack = []
        ele = intervals.pop()
        mystack.append(ele)

        while len(intervals) > 0:
            # pop ele from intervals
            ele = intervals.pop()

            # check if merge is possible..
            while len(mystack) > 0:
                if ele[1] >= mystack[-1][0]:
                    popped = mystack.pop()
                    ele = [ele[0], max(popped[1], ele[1])]
                else:
                    break
            mystack.append(ele)

            
        return mystack

        