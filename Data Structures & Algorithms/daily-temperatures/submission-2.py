class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mystack = []
        output = [0]*len(temperatures)

        for idx in range(len(temperatures)):
            temp = temperatures[idx]
            while len(mystack) > 0:
                if temp > temperatures[mystack[-1]]:
                    popped_idx = mystack.pop()
                    output[popped_idx] = idx - popped_idx
                else:
                    break
            mystack.append(idx)
        
        return output