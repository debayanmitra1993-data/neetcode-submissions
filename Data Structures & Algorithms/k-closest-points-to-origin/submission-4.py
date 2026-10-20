import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # (dist, idx) ... of size 'k'
        maxheap = []

        for idx in range(len(points)):
            x, y = points[idx]
            dist = x*x + y*y
            if len(maxheap) < k:
                heapq.heappush(maxheap, (-dist, idx))
            elif len(maxheap) >= k:
                if dist < -maxheap[0][0]:
                    heapq.heappop(maxheap)
                    heapq.heappush(maxheap, (-dist, idx))
        
        output = []
        for (dist, idx) in maxheap:
            output.append(points[idx])
        return output
        





        