class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for point in points:
            dis = self.compute_dist(point)
            self.push_to_maxheap((point, dis), k, maxheap)
        return [x[0] for x in maxheap]
    
    def compute_dist(self, point):
        return point[0]**2 + point[1]**2
    
    def push_to_maxheap(self, ele, k, maxheap):
        if len(maxheap) < k:
            maxheap.append(ele)
            self.siftUp(maxheap, len(maxheap) - 1)
        else:
            if ele[1] < maxheap[0][1]:
                maxheap[0] = ele
                self.siftDown(maxheap, 0, len(maxheap) - 1)
    
    def siftDown(self, maxheap, idx, endidx):
        c_idx_1 = (2*idx) + 1
        c_idx_2 = c_idx_1 + 1
        max_idx = idx
        if c_idx_1 <= endidx:
            if maxheap[c_idx_1][1] > maxheap[max_idx][1]:
                max_idx = c_idx_1
        if c_idx_2 <= endidx:
            if maxheap[c_idx_2][1] > maxheap[max_idx][1]:
                max_idx = c_idx_2
        if max_idx != idx:
            maxheap[max_idx], maxheap[idx] = maxheap[idx], maxheap[max_idx]
            self.siftDown(maxheap, max_idx, endidx)

    
    def siftUp(self, maxheap, idx):
        p_idx = (idx - 1) // 2
        while p_idx >= 0:
            if maxheap[idx][1] > maxheap[p_idx][1]:
                maxheap[idx], maxheap[p_idx] = maxheap[p_idx], maxheap[idx]
                idx = p_idx
                p_idx = (p_idx - 1) // 2
            else:
                break