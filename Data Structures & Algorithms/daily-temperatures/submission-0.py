class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0]*len(temperatures)
        tempstack = []
        tempstack.append(0)
        idx = 1

        while idx < len(temperatures):

            while temperatures[idx] > temperatures[tempstack[-1]]:
                stackidx = tempstack.pop()
                results[stackidx] = idx - stackidx
                if len(tempstack) == 0:
                    break
            
            tempstack.append(idx)
            idx += 1
        
        return results
            
