class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
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
        
        # check if the graph is fully connected
        visited = set()
        self.check_fully_connected(graph, 0, visited)
        if len(visited) != len(graph):
            return False
        
        # check if the graph has a cycle
        cycle_bool_lst = [False]
        visited = set()
        self.cycle_check(graph, 0, None, visited, cycle_bool_lst)
        if cycle_bool_lst[0] == True:
            return False
        
        return True
    
    def cycle_check(self, graph, node, parent, visited, cycle_bool_lst):
        visited.add(node)
        for child in graph[node]:
            if child in visited and child != parent:
                cycle_bool_lst[0] = True
                return
            if child not in visited:
                self.cycle_check(graph, child, node, visited, cycle_bool_lst)


    def check_fully_connected(self, graph, node, visited):
        if node in visited:
            return 
        
        visited.add(node)
        for child in graph[node]:
            if child not in visited:
                self.check_fully_connected(graph, child, visited)




        