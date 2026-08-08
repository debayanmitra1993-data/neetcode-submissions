class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxheap = []
        for ele in arr:
            self.push_to_maxheap(ele, maxheap, k, x)
        maxheap.sort(key = lambda x : x[0])
        return [x[0] for x in maxheap]

    def push_to_maxheap(self, ele, maxheap, k, x):
        point_dist = self.compute_dist(ele, x)
        if len(maxheap) < k:
            maxheap.append((ele, point_dist))
            self.siftUp(maxheap, len(maxheap) - 1)
        else:
            if point_dist < maxheap[0][1]:
                maxheap.append((ele, point_dist))
                maxheap[0], maxheap[len(maxheap) - 1] = maxheap[len(maxheap) - 1], maxheap[0]
                maxheap.pop()
                self.siftDown(0, maxheap, len(maxheap) - 1)
        

    def siftDown(self, idx, maxheap, endidx):
        c_idx_1, c_idx_2 = (2*idx) + 1, (2*idx) + 2
        max_idx = idx
        if c_idx_1 <= endidx:
            if maxheap[c_idx_1][1] > maxheap[max_idx][1]:
                max_idx = c_idx_1
        if c_idx_2 <= endidx:
            if maxheap[c_idx_2][1] > maxheap[max_idx][1]:
                max_idx = c_idx_2
        if max_idx != idx:
            maxheap[idx], maxheap[max_idx] = maxheap[max_idx], maxheap[idx]
            self.siftDown(max_idx, maxheap, endidx)
    
    def siftUp(self, maxheap, idx):
        p_idx = (idx - 1) // 2
        while p_idx >= 0:
            if maxheap[idx][1] > maxheap[p_idx][1]:
                maxheap[idx], maxheap[p_idx] = maxheap[p_idx], maxheap[idx]
                idx = p_idx
                p_idx = (p_idx - 1) // 2
            else:
                break    

    def compute_dist(self, ele, x):
        return abs(ele - x)

        
        