import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = {}
        maxpaths = {}
        for node in range(n):
            graph[node] = []
            maxpaths[node] = float("-inf")

        for idx in range(len(edges)):
            srcnode, destnode = edges[idx][0], edges[idx][1]
            prob_edge = succProb[idx]
            graph[srcnode].append((destnode, prob_edge))
            graph[destnode].append((srcnode, prob_edge))
        
        pq = []
        pq.append((-1.0, start_node))
        visited = set()
        while len(pq) > 0:
            probnode, node = heapq.heappop(pq)
            if node in visited:
                continue 
            if -probnode > maxpaths[node]:
                maxpaths[node] = -probnode
                for child in graph[node]:
                    childnode, childprobedge = child[0], child[1]
                    if childnode not in visited:
                        heapq.heappush(pq, (probnode * childprobedge, childnode))
            visited.add(node)
        # print("maxpaths = ", maxpaths)
        if maxpaths[end_node] == float("-inf"):
            return 0.0
        return maxpaths[end_node]