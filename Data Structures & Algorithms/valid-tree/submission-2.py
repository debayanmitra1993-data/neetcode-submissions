class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {}
        for node in range(n):
            graph[node] = []
        for edge in edges:
            src, dest = edge[0], edge[1]
            graph[src].append(dest)
            graph[dest].append(src)
        
        visited = set()
        cyclecheckbool = [False]
        self.dfstraversal(0, None, graph, visited, cyclecheckbool)
        return not cyclecheckbool[0] and len(visited) == n
    
    def dfstraversal(self, node, parentnode, graph, visited, cyclecheckbool):
        visited.add(node)

        if cyclecheckbool[0] == True:
            return 

        for childnode in graph[node]:
            if childnode in visited and childnode != parentnode and parentnode is not None:
                cyclecheckbool[0] = True
                return 

            if childnode not in visited:
                self.dfstraversal(childnode, node, graph, visited, cyclecheckbool)
