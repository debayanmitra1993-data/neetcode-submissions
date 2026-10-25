import heapq

class Solution:
    def checkconnectivity(self, graph, node, visited):
        visited.add(node)
        for childnode, _ in graph[node]:
            if childnode not in visited:
                self.checkconnectivity(graph, childnode, visited)
        
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for node in range(n):
            graph[node] = []
        for src,dest,wt in edges:
            graph[src].append((dest, wt))
            graph[dest].append((src, wt))
        
        visited = set()
        self.checkconnectivity(graph, 0, visited)
        if len(visited) < n:
            return -1

        mstpq = []
        visited = set()
        for dst, wt in graph[0]:
            pq_tuple = (wt, 0, dst) # (edgeweight, src, dest)
            heapq.heappush(mstpq, pq_tuple)
        visited.add(0)

        mstsum = 0

        while len(mstpq) > 0:
            wt, src, dest = heapq.heappop(mstpq)
            if dest in visited:
                continue
            else:
                mstsum += wt 
                for childnode, wt in graph[dest]:
                    if childnode not in visited:
                        heapq.heappush(mstpq, (wt, dest ,childnode))
                visited.add(dest)
        return mstsum
