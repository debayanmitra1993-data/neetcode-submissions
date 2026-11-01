class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        sp = {}
        for node in range(n):
            graph[node] = []
            sp[node] = float("inf")
        
        for srcnode, dstnode, dist in flights:
            graph[srcnode].append((dstnode, dist))
        
        q = []
        sp[src] = 0
        for childnode, childwt in graph[src]:
            q.append((childnode, childwt))
        
        stops = -1
        while stops < k:
            newq = []
            while len(q) > 0:
                node, dist = q.pop()
                if dist < sp[node]:
                    sp[node] = dist
                    for childnode, childwt in graph[node]:
                        newq.append((childnode, dist + childwt))
            q = newq.copy()
            # print("q = ", q)
            stops += 1
        
        return sp[dst] if sp[dst] != float("inf") else -1