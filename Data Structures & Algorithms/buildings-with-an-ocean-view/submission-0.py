class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []

        for idx in range(len(heights)):
            height = heights[idx]
            while len(stack) > 0:
                if height >= heights[stack[-1]]:
                    popped_idx = stack.pop()
                else:
                    break
            stack.append(idx)
        
        return stack