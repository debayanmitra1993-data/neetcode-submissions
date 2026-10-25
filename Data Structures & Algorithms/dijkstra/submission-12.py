import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = {}
        shortest_paths = {}
        for node in range(n):
            graph[node] = []
            shortest_paths[node] = float("inf")
        shortest_paths[src] = 0

        for srcnode, destnode, wt in edges:
            graph[srcnode].append((destnode, wt))
        
        pq = []
        for childnode, wt in graph[src]:
            heapq.heappush(pq, (wt, childnode))
        
        while len(pq) > 0:
            wt, node = heapq.heappop(pq)
            if wt < shortest_paths[node]:
                shortest_paths[node] = wt 
                for childnode, childwt in graph[node]:
                    heapq.heappush(pq, (childwt + wt, childnode))
        
        for node in shortest_paths.keys():
            if shortest_paths[node] == float("inf"):
                shortest_paths[node] = -1
        
        return shortest_paths