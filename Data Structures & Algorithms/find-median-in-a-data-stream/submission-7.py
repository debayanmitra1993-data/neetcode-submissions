class MedianFinder:
    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        self.push_to_heap("max", num)
        if len(self.maxheap) > 0 and len(self.minheap) > 0:
            if self.maxheap[0] > self.minheap[0]:
                pop_max = self.pop_from_heap("max")
                self.push_to_heap("min", pop_max)
        if len(self.maxheap) - len(self.minheap) > 1:
            pop_max = self.pop_from_heap("max")
            self.push_to_heap("min", pop_max)
        if len(self.minheap) - len(self.maxheap) > 1:
            pop_min = self.pop_from_heap("min")
            self.push_to_heap("max", pop_min)


    def findMedian(self) -> float:
        print("minheap = ", self.minheap)
        print("maxheap = ", self.maxheap)
        if len(self.minheap) == 0:
            return self.maxheap[0]
    
        if (len(self.maxheap) + len(self.minheap)) % 2 == 0:
            return (self.maxheap[0] + self.minheap[0])/2
        else:
            if len(self.maxheap) > len(self.minheap):
                return self.maxheap[0]
            else:
                return self.minheap[0]
    
    def pop_from_heap(self, mode):
        if mode == "max":
            self.maxheap[0], self.maxheap[len(self.maxheap) - 1] = self.maxheap[len(self.maxheap) - 1], self.maxheap[0]
            popped_ele = self.maxheap.pop()
            self.siftDown(0, len(self.maxheap) - 1, "max")
            return popped_ele
        elif mode == "min":
            self.minheap[0], self.minheap[len(self.minheap) - 1] = self.minheap[len(self.minheap) - 1], self.minheap[0]
            popped_ele = self.minheap.pop()
            self.siftDown(0, len(self.minheap) - 1, "min")
            return popped_ele
    
    def siftDown(self, idx, endidx, mode):
        if mode == "max":
            child_idx_1 = (2*idx) + 1
            child_idx_2 = (2*idx) + 2
            max_idx = idx
            if child_idx_1 <= endidx:
                if self.maxheap[child_idx_1] > self.maxheap[idx]:
                    max_idx = child_idx_1
            if child_idx_2 <= endidx:
                if self.maxheap[child_idx_2] > self.maxheap[max_idx]:
                    max_idx = child_idx_2
            if max_idx != idx:
                self.maxheap[idx], self.maxheap[max_idx] = self.maxheap[max_idx], self.maxheap[idx]
                self.siftDown(max_idx, endidx, "max")
        elif mode == "min":
            child_idx_1 = (2*idx) + 1
            child_idx_2 = (2*idx) + 2
            min_idx = idx
            if child_idx_1 <= endidx:
                if self.minheap[child_idx_1] < self.minheap[idx]:
                    min_idx = child_idx_1
            if child_idx_2 <= endidx:
                if self.minheap[child_idx_2] < self.minheap[min_idx]:
                    min_idx = child_idx_2
            if min_idx != idx:
                self.minheap[idx], self.minheap[min_idx] = self.minheap[min_idx], self.minheap[idx]
                self.siftDown(min_idx, endidx, "min")

    def push_to_heap(self, mode, val):
        if mode == "max":
            if len(self.maxheap) == 0:
                self.maxheap.append(val)
                return 
            self.maxheap.append(val)
        elif mode == "min":
            if len(self.minheap) == 0:
                self.minheap.append(val)
                return 
            self.minheap.append(val)
        self.siftUp(mode)
    
    def siftUp(self, mode):
        if mode == "max":
            idx = len(self.maxheap) - 1
        elif mode == "min":
            idx = len(self.minheap) - 1
        
        p_idx = (idx - 1) // 2
        while p_idx >= 0:
            if mode == "max":
                if self.maxheap[idx] > self.maxheap[p_idx]:
                    self.maxheap[idx], self.maxheap[p_idx] = self.maxheap[p_idx], self.maxheap[idx]
                    idx = p_idx 
                    p_idx = (p_idx - 1) // 2
                else:
                    break
            elif mode == "min":
                if self.minheap[idx] < self.minheap[p_idx]:
                    self.minheap[idx], self.minheap[p_idx] = self.minheap[p_idx], self.minheap[idx]
                    idx = p_idx
                    p_idx = (p_idx - 1) // 2
                else:
                    break
