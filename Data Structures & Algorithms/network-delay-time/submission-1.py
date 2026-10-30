import heapq 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        sp = {}
        graph = {}

        for node in range(1, n + 1):
            graph[node] = []
            sp[node] = float("inf")
        for src, dst, wt in times:
            graph[src].append((dst, wt))
        
        pq = []
        for node, wt in graph[k]:
            heapq.heappush(pq, (wt, node))
        sp[k] = 0
        
        while len(pq) > 0:
            wt, node = heapq.heappop(pq)
            if wt < sp[node]:
                sp[node] = wt
                for childnode, childwt in graph[node]:
                    heapq.heappush(pq, (wt + childwt, childnode))
        
        maxtime = 0
        for node in sp.keys():
            if sp[node] == float("inf"):
                return -1
                
            if node != k:
                if sp[node] > maxtime:
                    maxtime = sp[node]
        return maxtime 
        