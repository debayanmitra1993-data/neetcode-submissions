class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mystack = [(0, heights[0])]
        maxarea = 0

        for idx in range(1, len(heights)):
            ele = heights[idx]
            if ele >= mystack[-1][1]:
                mystack.append((idx, ele))
            else:
                while len(mystack) > 0:
                    if ele < mystack[-1][1]:
                        popped_idx, popped_ele = mystack.pop()
                        area = popped_ele * (idx - popped_idx)
                        if area > maxarea:
                            maxarea = area        
                    else:
                        break
                mystack.append((popped_idx, ele))
        
        n = len(heights)
        while len(mystack) > 0:
            popped_idx, popped_ele = mystack.pop()
            area = popped_ele * (n - popped_idx)
            if area > maxarea:
                maxarea = area
        return maxarea





        