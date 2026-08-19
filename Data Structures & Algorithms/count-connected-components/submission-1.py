class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for node in range(n):
            graph[node] = []
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visited = set()
        n_conn = 0
        
        while len(visited) < n:
            for node in range(n):
                if node not in visited:
                    self.recursivedfs(node, visited, graph)
                    break
            n_conn += 1
        return n_conn
    
    def recursivedfs(self, node, visited, graph):
        visited.add(node)
        for childnode in graph[node]:
            if childnode not in visited:
                self.recursivedfs(childnode, visited, graph)




        
        