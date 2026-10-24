class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []
        self.graph[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        wasremoved = False
        if src in self.graph:
            if dst in self.graph[src]:
                self.graph[src].remove(dst)
                wasremoved = True
        return wasremoved

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        self.dfsrecursion(src, visited, self.graph)
        if dst in visited:
            return True
        else:
            return False
    
    def dfsrecursion(self, node, visited, graph):
        if node in visited:
            return 
        
        visited.add(node)
        for childnode in graph[node]:
            if childnode not in visited:
                self.dfsrecursion(childnode, visited, graph)

