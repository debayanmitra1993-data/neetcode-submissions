import heapq

class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)
        
        # condition check (maxheap[0] >= minheap[0])
        if len(self.minheap) > 0:
            if self.minheap[0] < -self.maxheap[0]:
                pop_ele_from_maxheap = heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, -pop_ele_from_maxheap)
        
        # condition check (length diff > 1)
        if len(self.maxheap) - len(self.minheap) > 1:
            if len(self.maxheap) > 0:
                pop_ele_from_maxheap = heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, -pop_ele_from_maxheap)
        elif len(self.minheap) - len(self.maxheap) > 1:
            if len(self.minheap) > 0:
                pop_ele_from_minheap = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -pop_ele_from_minheap)

    def findMedian(self) -> float:
        if len(self.minheap) == 0:
            return -self.maxheap[0]
        
        totlen = len(self.minheap) + len(self.maxheap)

        if totlen % 2 == 0:
            return 0.5*(self.minheap[0] - self.maxheap[0])
        else:
            if len(self.maxheap) > len(self.minheap):
                return -self.maxheap[0]
            else:
                return self.minheap[0]