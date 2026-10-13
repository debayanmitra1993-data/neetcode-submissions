import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    neg_nums = [-ele for ele in nums]
    heapq.heapify(neg_nums)
    out = []
    while len(neg_nums) > 0:
        ele = heapq.heappop(neg_nums)
        out.append(-ele)
    return out

# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
