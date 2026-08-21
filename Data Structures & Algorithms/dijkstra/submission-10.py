import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = {}
        shortest_paths = {}
        for node in range(n):
            graph[node] = []
            shortest_paths[node] = float("inf")
        for edge in edges:
            srcnode, destnode, wt = edge[0], edge[1], edge[2]
            graph[srcnode].append((destnode, wt))

        pq = []
        pq.append((src, 0))
        
        while len(pq) > 0:
            popped_node, dist = heapq.heappop(pq)
            if dist < shortest_paths[popped_node]:
                shortest_paths[popped_node] = dist
                for child in graph[popped_node]:
                    childnode, wt = child[0], child[1]
                    heapq.heappush(pq, (childnode, wt + shortest_paths[popped_node]))
        for node in shortest_paths.keys():
            if shortest_paths[node] == float("inf"):
                shortest_paths[node] = -1
        return shortest_paths