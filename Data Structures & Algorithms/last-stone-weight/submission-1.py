class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # convert stones to max heap..O(n) time 
        self.buildmaxheap(stones)
        print("stones max heap = ", stones)

        while len(stones) > 1:
            stones[0], stones[len(stones) - 1] = stones[len(stones) - 1], stones[0]
            top_ele = stones.pop()
            self.siftDown(0, len(stones) - 1, stones)

            stones[0], stones[len(stones) - 1] = stones[len(stones) - 1], stones[0]
            bottom_ele = stones.pop()
            self.siftDown(0, len(stones) - 1, stones)

            if top_ele == bottom_ele:
                continue 
            else:
                stones.append(top_ele - bottom_ele)
                self.siftUp(len(stones) - 1, stones)
        
        if len(stones) == 0:
            return 0 
        else:
            return stones[0]
    
    def siftUp(self, idx, stones):
        p_idx = (idx - 1) // 2
        while p_idx >= 0:
            if stones[idx] > stones[p_idx]:
                stones[idx], stones[p_idx] = stones[p_idx], stones[idx]
                idx = p_idx
                p_idx = (p_idx - 1) // 2
            else:
                break
    
    def buildmaxheap(self, stones):
        last_internal_node_idx = (len(stones) - 2) // 2
        for idx in range(last_internal_node_idx, -1, -1):
            self.siftDown(idx, len(stones) - 1, stones)
    
    def siftDown(self, idx, endidx, stones):
        child_idx_1 = (2*idx) + 1
        child_idx_2 = child_idx_1 + 1

        max_idx = idx
        if child_idx_1 <= endidx:
            if stones[child_idx_1] > stones[idx]:
                max_idx = child_idx_1
        if child_idx_2 <= endidx:
            if stones[child_idx_2] > stones[max_idx]:
                max_idx = child_idx_2
        if max_idx != idx:
            stones[idx], stones[max_idx] = stones[max_idx], stones[idx]
            self.siftDown(max_idx, endidx, stones)
        

        