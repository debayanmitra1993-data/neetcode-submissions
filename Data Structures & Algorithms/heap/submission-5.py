class MinHeap:
    
    def __init__(self):
        self.minheap = []

    def push(self, val: int) -> None:
        self.minheap.append(val)
        self.siftUp(len(self.minheap) - 1)
    
    def siftUp(self, idx):
        p_idx = (idx - 1)//2
        while p_idx >= 0:
            if self.minheap[idx] < self.minheap[p_idx]:
                self.minheap[idx], self.minheap[p_idx] = self.minheap[p_idx], self.minheap[idx]
                idx = p_idx
                p_idx = (p_idx - 1) // 2
            else:
                break

    def pop(self) -> int:
        if len(self.minheap) == 0:
            return -1
        self.minheap[0], self.minheap[-1] = self.minheap[-1], self.minheap[0]
        popped_ele = self.minheap.pop()
        self.siftDown(0, len(self.minheap) - 1)
        return popped_ele
    
    def siftDown(self, idx, endidx):
        child_idx_1 = (2*idx) + 1
        child_idx_2 = (2*idx) + 2
        min_idx = idx
        if child_idx_1 <= endidx:
            if self.minheap[child_idx_1] < self.minheap[min_idx]:
                min_idx = child_idx_1
        if child_idx_2 <= endidx:
            if self.minheap[child_idx_2] < self.minheap[min_idx]:
                min_idx = child_idx_2
        if min_idx != idx:
            self.minheap[idx], self.minheap[min_idx] = self.minheap[min_idx], self.minheap[idx]
            self.siftDown(min_idx, endidx)

    def top(self) -> int:
        if len(self.minheap) == 0:
            return -1
        return self.minheap[0]

    def heapify(self, nums: List[int]) -> None:
        self.minheap = nums
        last_idx = len(nums) - 1
        last_internal_node_idx = (last_idx - 1) // 2
        for idx in range(last_internal_node_idx, -1, -1):
            self.siftDown(idx, last_idx)
        