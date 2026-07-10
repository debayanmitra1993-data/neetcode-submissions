class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0]*len(temperatures)
        monotonic_decreasing_stack = []
        monotonic_decreasing_stack.append(0)
        idx = 1
        while idx < len(temperatures):
            while temperatures[idx] > temperatures[monotonic_decreasing_stack[-1]]:
                popped_idx = monotonic_decreasing_stack.pop()
                results[popped_idx] = idx - popped_idx
                if len(monotonic_decreasing_stack) == 0:
                    break
            monotonic_decreasing_stack.append(idx)
            idx += 1
        return results
        




        