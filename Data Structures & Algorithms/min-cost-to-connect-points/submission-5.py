class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0

        # undirected graph (any one edge is enough)
        # edges = []
        graph = {}

        for idx in range(len(points) - 1):
            for jdx in range(idx + 1, len(points)):
                point1, point2 = points[idx], points[jdx]
                dist_pts = self.dist_bw_pts(point1, point2)
                # edges.append([idx, jdx, dist_pts])
                if idx not in graph:
                    graph[idx] = []
                if jdx not in graph:
                    graph[jdx] = []
                graph[idx].append([jdx, dist_pts])
                graph[jdx].append([idx, dist_pts])
        
        visited = set()
        visited.add(0)
        minheap = []
        for edge in graph[0]:
            self.push_to_minheap([0] + edge, minheap)
        mst = 0

        while len(minheap) > 0 and len(visited) < len(points):
            popped_edge = self.pop_from_minheap(minheap)
            src, dest, wt = popped_edge[0], popped_edge[1], popped_edge[2]
            if dest in visited:
                continue 

            visited.add(dest)
            mst += wt 
            for child in graph[dest]:
                if child[0] not in visited:
                    self.push_to_minheap([dest] + child, minheap)
        return mst
    
    def pop_from_minheap(self, minheap):
        minheap[0], minheap[len(minheap) - 1] = minheap[len(minheap) - 1], minheap[0]
        ele = minheap.pop()
        self.siftDown(0, len(minheap) - 1, minheap)
        return ele
    
    def siftDown(self, idx, endidx, minheap):
        child_idx_1 = (2*idx) + 1
        child_idx_2 = (2*idx) + 2
        min_idx = idx
        if child_idx_1 <= endidx:
            if minheap[child_idx_1][2] < minheap[idx][2]:
                min_idx = child_idx_1
        if child_idx_2 <= endidx:
            if minheap[child_idx_2][2] < minheap[min_idx][2]:
                min_idx = child_idx_2
        if min_idx != idx:
            minheap[min_idx], minheap[idx] = minheap[idx], minheap[min_idx]
            self.siftDown(min_idx, endidx, minheap)

    def push_to_minheap(self, edge, minheap):
        if len(minheap) == 0:
            minheap.append(edge)
            return 
        minheap.append(edge)
        self.siftUp(len(minheap) - 1, minheap)
    
    def siftUp(self, idx, minheap):
        p_idx = (idx - 1) // 2
        while p_idx >= 0:
            if minheap[idx][2] < minheap[p_idx][2]:
                minheap[idx], minheap[p_idx] = minheap[p_idx], minheap[idx]
                idx = p_idx
                p_idx = (p_idx - 1)//2
            else:
                break

    def dist_bw_pts(self, p1, p2):
        return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
    




        