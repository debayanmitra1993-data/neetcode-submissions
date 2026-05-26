class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = []
        for ele in nums:
            self.add(ele)

    def add(self, val: int) -> int:
        k = self.k
        if len(self.minheap) < k:
            self.minheap.append(val)
            self.siftUp(len(self.minheap) - 1)
            return self.minheap[0]
        elif len(self.minheap) == k:
            if val <= self.minheap[0]:
                return self.minheap[0]
            else:
                self.minheap[0], self.minheap[k - 1] = self.minheap[k - 1], self.minheap[0]
                self.siftDown(0, k - 2)
                self.minheap[k - 1] = val
                self.siftUp(k - 1)
                return self.minheap[0]
    
    def siftDown(self, idx, endidx):
        child_idx_1, child_idx_2 = (2*idx) + 1, (2*idx) + 2
        min_idx = idx 
        if child_idx_1 <= endidx:
            if self.minheap[child_idx_1] < self.minheap[idx]:
                min_idx = child_idx_1
        if child_idx_2 <= endidx:
            if self.minheap[child_idx_2] < self.minheap[min_idx]:
                min_idx = child_idx_2
        if idx != min_idx:
            self.minheap[idx], self.minheap[min_idx] = self.minheap[min_idx], self.minheap[idx]
            self.siftDown(min_idx, endidx)

    def siftUp(self, idx):
        p_idx = (idx - 1) // 2 
        while p_idx >= 0:
            if self.minheap[idx] < self.minheap[p_idx]:
                self.minheap[idx], self.minheap[p_idx] = self.minheap[p_idx], self.minheap[idx]
                idx = p_idx 
                p_idx = (idx - 1) // 2 
            else:
                break

        
