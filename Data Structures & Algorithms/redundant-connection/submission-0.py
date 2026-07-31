class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        for edge in edges:
            src, dest = edge[0], edge[1]
            if src not in graph:
                graph[src] = []
            if dest not in graph:
                graph[dest] = []
            graph[src].append(dest)
            graph[dest].append(src)
        
        for idx in range(len(edges) - 1, -1, -1):
            edge = edges[idx]
            src, dest = edge[0], edge[1]
            graph[src].remove(dest)
            graph[dest].remove(src)

            if self.check_graph_connectivity(graph) == True:
                return edge
            else:
                graph[src].append(dest)
                graph[dest].append(src)
    
    def check_graph_connectivity(self, graph):
        visited = set()
        self.dfs(1, visited, graph)
        if len(visited) == len(graph):
            return True
        else:
            return False
    
    def dfs(self, node, visited, graph):
        visited.add(node)
        for child in graph[node]:
            if child not in visited:
                self.dfs(child, visited, graph)