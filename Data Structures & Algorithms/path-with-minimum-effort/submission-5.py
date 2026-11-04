import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        sp = {}
        for rowidx in range(len(heights)):
            for colidx in range(len(heights[rowidx])):
                sp[(rowidx, colidx)] = float("inf")
        
        visited = set()
        pq = []
        heapq.heappush(pq, (0, 0, 0))

        while len(pq) > 0:
            dist, rowidx, colidx = heapq.heappop(pq)
            if (rowidx, colidx) in visited:
                continue 
            
            if dist < sp[(rowidx, colidx)]:
                sp[(rowidx, colidx)] = dist 

                if self.isvalidcell(rowidx + 1, colidx, visited, heights):
                    heapq.heappush(pq, (max(
                        dist, 
                        abs(heights[rowidx][colidx] - heights[rowidx + 1][colidx])
                    ), rowidx + 1, colidx))

                if self.isvalidcell(rowidx - 1, colidx, visited, heights):
                    heapq.heappush(pq, (max(
                        dist, 
                        abs(heights[rowidx][colidx] - heights[rowidx - 1][colidx])
                    ), rowidx - 1, colidx))
                
                if self.isvalidcell(rowidx, colidx - 1, visited, heights):
                    heapq.heappush(pq, (max(
                        dist, 
                        abs(heights[rowidx][colidx] - heights[rowidx][colidx - 1])
                    ), rowidx, colidx - 1))
                
                if self.isvalidcell(rowidx, colidx + 1, visited, heights):
                    heapq.heappush(pq, (max(
                        dist, 
                        abs(heights[rowidx][colidx] - heights[rowidx][colidx + 1])
                    ), rowidx, colidx + 1))
                
                visited.add((rowidx, colidx))
        return sp[(len(heights) - 1, len(heights[0]) - 1)]
                
    
    def isvalidcell(self, rowidx, colidx, visited, heights):
        if rowidx < 0 or colidx < 0 or rowidx > len(heights) - 1 or colidx > len(heights[0]) - 1:
            return False
        if (rowidx, colidx) in visited:
            return False
        return True
