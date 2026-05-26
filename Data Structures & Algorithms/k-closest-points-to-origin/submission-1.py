class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_maxheap = []
        for point in points:
            self.push(point, k_maxheap, k)
        
        return k_maxheap
    
    def push(self, point, k_maxheap, k):
        if len(k_maxheap) < k:
            k_maxheap.append(point)
            self.siftUp(len(k_maxheap) - 1, k_maxheap)
        elif len(k_maxheap) == k:
            max_heap_ele = k_maxheap[0]
            print("max_heap_ele = ", max_heap_ele)
            if self.dist_from_origin(point[0], point[1]) < self.dist_from_origin(max_heap_ele[0], max_heap_ele[1]):
                k_maxheap[0], k_maxheap[len(k_maxheap) - 1] = k_maxheap[len(k_maxheap) - 1], k_maxheap[0]
                k_maxheap.pop()
                self.siftDown(0, len(k_maxheap) - 1, k_maxheap)
                k_maxheap.append(point)
                self.siftUp(len(k_maxheap) - 1, k_maxheap)
            else:
                pass
    
    def siftDown(self, idx, endidx, k_maxheap):
        child_idx_1, child_idx_2 = (2*idx) + 1, (2*idx) + 2
        max_idx = idx
        if child_idx_1 <= len(k_maxheap) - 1:
            if self.dist_from_origin(k_maxheap[child_idx_1][0], k_maxheap[child_idx_1][1]) > self.dist_from_origin(k_maxheap[idx][0], k_maxheap[idx][1]):
                max_idx = child_idx_1
        if child_idx_2 <= len(k_maxheap) - 1:
            if self.dist_from_origin(k_maxheap[child_idx_2][0], k_maxheap[child_idx_2][1]) > self.dist_from_origin(k_maxheap[max_idx][0], k_maxheap[max_idx][1]):
                max_idx = child_idx_2 
        if max_idx != idx:
            k_maxheap[idx], k_maxheap[max_idx] = k_maxheap[max_idx], k_maxheap[idx]
            self.siftDown(max_idx, endidx, k_maxheap) 


                 
    def dist_from_origin(self, x, y):
        return x*x + y*y
    
    def siftUp(self, idx, k_maxheap):
        p_idx = (idx - 1) // 2 
        while p_idx >= 0:
            if self.dist_from_origin(k_maxheap[idx][0], k_maxheap[idx][1]) > self.dist_from_origin(k_maxheap[p_idx][0], k_maxheap[p_idx][1]):
                k_maxheap[idx], k_maxheap[p_idx] = k_maxheap[p_idx], k_maxheap[idx]
                idx = p_idx 
                p_idx = (p_idx - 1) // 2 
            else:
                break

        