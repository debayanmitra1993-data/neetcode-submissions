import heapq

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for node in range(n):
            graph[node] = []
        for edge in edges:
            src, dest, wt = edge[0], edge[1], edge[2]
            graph[src].append((dest, wt))
            graph[dest].append((src, wt))
        
        # check if graph is connected or not..
        visited = set()
        self.dfstraversal(0, visited, graph)
        if len(visited) < n:
            return -1
        
        pq = [] # (wt, src, dest)
        visited = set()
        for edge in graph[0]:
            heapq.heappush(pq, (edge[1], 0, edge[0]))
        visited.add(0)
        mstval = 0

        while len(pq) > 0:
            wt, src, dest = heapq.heappop(pq)
            if dest not in visited:
                mstval += wt
                for child in graph[dest]:
                    child_dest, child_wt = child[0], child[1]
                    if child_dest not in visited:
                        heapq.heappush(pq, (child_wt, dest, child_dest))
                visited.add(dest)
            else:
                continue
        return mstval
    
    def dfstraversal(self, node, visited, graph):
        visited.add(node)
        for child in graph[node]:
            if child[0] not in visited:
                self.dfstraversal(child[0], visited, graph)