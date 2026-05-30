class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
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
        
        # check if di-graph has a cycle or not, if it has - return []
        cycle_lst = [False]
        has_cycle = self.cycle_check(graph, set(), set(), 0, cycle_lst)
        if cycle_lst[0] == True:
            return []
        
        visited = set()
        top_sort = []
        while len(visited) < len(graph):
            for node in graph.keys():
                if node not in visited:
                    src_node = node
                    break
            
            self.dfspostorder(src_node, visited, top_sort, graph)
        top_sort.reverse()
        return top_sort

    def dfspostorder(self, node, visited, top_sort, graph):
        for childnode in graph[node]:
            if childnode not in visited:
                self.dfspostorder(childnode, visited, top_sort, graph)
        if node not in visited:
            visited.add(node)
            top_sort.append(node) 
    
    def cycle_check(self, graph, visited, path, node, cycle_lst):
        if node in path:
            cycle_lst[0] = True
            return 
        
        if node in visited:
            return 
        
        visited.add(node)
        path.add(node)
        for childnode in graph[node]:
            self.cycle_check(graph, visited, path, childnode, cycle_lst)
        path.remove(node)