from collections import deque 
      
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        maxout = []
        for idx in range(k):
            ele = nums[idx]
            while len(q) > 0:
                if ele >= q[-1][1]:
                    _, _ = q.pop()
                else:
                    break
            q.append((idx, ele))
        maxout.append(q[0][1])

        for idx in range(k, len(nums)):
            ele = nums[idx]
            while len(q) > 0:
                if ele >= q[-1][1]:
                    _, _ = q.pop()
                else:
                    break
            q.append((idx, ele))
            if idx - q[0][0] >= k:
                _, _ = q.popleft()
            maxout.append(q[0][1])
        return maxout





        