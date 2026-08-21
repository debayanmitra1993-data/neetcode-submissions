class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        for node in range(n):
            graph[node] = []
        for edge in edges:
            src, dest = edge[0], edge[1]
            graph[src].append(dest)
        visited = set()
        path = set()
        cyclebool = [False]
        self.cyclecheckdigraph(graph, node, visited, path, cyclebool)
        if cyclebool[0] == True:
            return []
        
        visited = set()
        out = [] 
        while len(visited) < n:
            for node in range(n):
                if node not in visited:
                    self.postorderdfs(node, visited, graph, out)
        out.reverse()
        return out

    def postorderdfs(self, node, visited, graph, out):
        visited.add(node)
        for childnode in graph[node]:
            if childnode not in visited:
                self.postorderdfs(childnode, visited, graph, out)
        out.append(node)
    
    def cyclecheckdigraph(self, graph, node, visited, path, cyclebool):
        visited.add(node)
        path.add(node)
        for childnode in graph[node]:
            if childnode in visited and childnode in path:
                cyclebool[0] = True
                return 
            if childnode not in visited:
                self.cyclecheckdigraph(graph, childnode, visited, path, cyclebool)
        path.remove(node)