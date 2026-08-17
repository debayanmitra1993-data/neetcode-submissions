from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # create the first slide - monotonic queue
        mq = deque()
        for idx in range(k):
            ele = nums[idx]
            if len(mq) == 0:
                mq.append(idx)
            else:
                if ele <= nums[mq[-1]]:
                    mq.append(idx)
                else:
                    while len(mq) > 0:
                        if ele > nums[mq[-1]]:
                            popped_ele = mq.pop()
                        else:
                            break
                    mq.append(idx)
        
        out = [0]*(len(nums) - k + 1)

        for idx in range(len(out)):
            if idx == 0:
                out[idx] = nums[mq[0]]
                if mq[0] == idx:
                    popped = mq.popleft()           
            else:
                insert_idx = idx + k - 1
                ele = nums[insert_idx]
                if len(mq) == 0:
                    mq.append(insert_idx)
                else:
                    if ele <= nums[mq[-1]]:
                        mq.append(insert_idx)
                    else:
                        while len(mq) > 0:
                            if ele > nums[mq[-1]]:
                                popped_ele = mq.pop()
                            else:
                                break
                        mq.append(insert_idx)
                out[idx] = nums[mq[0]]
                if mq[0] == idx:
                    popped = mq.popleft()
        return out