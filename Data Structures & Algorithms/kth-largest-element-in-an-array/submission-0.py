class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_minheap = []
        for ele in nums:
            self.push(ele, k_minheap, k)
        return k_minheap[0]
    
    def push(self, ele, k_minheap, k):
        if len(k_minheap) < k:
            k_minheap.append(ele)
            self.siftUp(len(k_minheap) - 1, k_minheap)
        elif len(k_minheap) == k:
            if ele <= k_minheap[0]:
                pass
            else:
                k_minheap[0], k_minheap[len(k_minheap) - 1] = k_minheap[len(k_minheap) - 1], k_minheap[0]
                k_minheap.pop()
                self.siftDown(0, len(k_minheap) - 1, k_minheap)
                k_minheap.append(ele)
                self.siftUp(len(k_minheap) - 1, k_minheap)
    
    def siftDown(self, idx, endidx, k_minheap):
        child_idx_1 , child_idx_2 = (2*idx) + 1, (2*idx) + 2 
        min_idx = idx
        if child_idx_1 <= len(k_minheap) - 1:
            if k_minheap[child_idx_1] < k_minheap[idx]:
                min_idx = child_idx_1
        if child_idx_2 <= len(k_minheap) - 1:
            if k_minheap[child_idx_2] < k_minheap[min_idx]:
                min_idx = child_idx_2
        if idx != min_idx:
            k_minheap[min_idx], k_minheap[idx] = k_minheap[idx], k_minheap[min_idx]
            self.siftDown(min_idx, endidx, k_minheap)
    
    def siftUp(self, idx, k_minheap):
        p_idx = (idx - 1) // 2 
        while p_idx >= 0:
            if k_minheap[idx] < k_minheap[p_idx]:
                k_minheap[idx], k_minheap[p_idx] = k_minheap[p_idx], k_minheap[idx]
                idx = p_idx
                p_idx = (p_idx - 1) // 2 
            else:
                break 
        
        
        


        