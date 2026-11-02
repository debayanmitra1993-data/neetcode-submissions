class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        stack.append(0) # (idx)

        for idx in range(1, len(temperatures)):
            temp = temperatures[idx]
            while len(stack) > 0:
                if temp > temperatures[stack[-1]]:
                    popped_idx = stack.pop()
                    res[popped_idx] = idx - popped_idx
                else:
                    break
            stack.append(idx)
        
        return res
        