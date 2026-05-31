class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for node in range(n):
            graph[node] = []
        for edge in edges:
            src, dest = edge[0], edge[1]
            if src not in graph:
                graph[src] = []
            if dest not in graph:
                graph[dest] = []
            graph[src].append(dest)
            graph[dest].append(src)
        
        visited = set()
        count_conn = 0

        while len(visited) < n:
            for node in graph.keys():
                if node not in visited:
                    src = node
                    break
            
            self.dfs(graph, visited, src)
            count_conn += 1
        
        return count_conn
    
    def dfs(self, graph, visited, node):
        if node in visited:
            return 
        
        visited.add(node)
        for child in graph[node]:
            self.dfs(graph, visited, child)