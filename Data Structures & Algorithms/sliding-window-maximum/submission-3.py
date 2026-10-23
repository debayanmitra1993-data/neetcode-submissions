from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque()
        out = []

        for idx in range(k):
            ele = nums[idx]
            if len(q) == 0:
                q.append((idx, ele))
            else:
                while len(q) > 0:
                    if ele > q[-1][1]:
                        q.pop()
                    else:
                        break
                q.append((idx, ele))
        
        out.append(q[0][1])

        for idx in range(1, n - k + 1):
            # pop out any out of index ele from queue...
            if q[0][0] < idx:
                q.popleft()
            
            # new ele to add..
            ele = nums[idx + k - 1]
            while len(q) > 0:
                if ele > q[-1][1]:
                    q.pop()
                else:
                    break
            q.append((idx + k - 1, ele))
            
            # fetch the max (front of queue) for the max in this window..
            # print("idx:", idx, "deque:", list(q), "max:", q[0][1])
            out.append(q[0][1])
    
        return out
        
        