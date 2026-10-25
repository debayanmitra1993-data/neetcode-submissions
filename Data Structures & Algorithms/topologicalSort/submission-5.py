class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        for node in range(n):
            graph[node] = []
        for src, dest in edges:
            graph[src].append(dest)
        
        hascyclelst = [False]
        visited = set()
        for node in graph.keys():
            if node not in visited:
                path = set()
                self.dfs(graph, node, visited, path, hascyclelst)
                if hascyclelst[0] == True:
                    return []
        
        output = []
        visited = set()
        for node in graph.keys():
            if node not in visited:
                self.postorderdfs(graph, output, visited, node)
        return output[::-1]
    
    def postorderdfs(self, graph, output, visited, node):
        for childnode in graph[node]:
            if childnode not in visited:
                self.postorderdfs(graph, output, visited, childnode)
        output.append(node)
        visited.add(node)
        
    def dfs(self, graph, node, visited, path, hascyclelst):
        if hascyclelst[0] == True:
            return 

        path.add(node)

        for childnode in graph[node]:
            if childnode in path:
                hascyclelst[0] = True
                return
            if childnode not in visited:
                self.dfs(graph, childnode, visited, path, hascyclelst)
        
        visited.add(node)
        path.remove(node)
