class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for node in range(numCourses):
            graph[node] = []
        for edge in prerequisites:
            dest, src = edge[0], edge[1]
            if src not in graph:
                graph[src] = []
            if dest not in graph:
                graph[dest] = []
            graph[src].append(dest)
        
        visited = set()
        while len(visited) < numCourses:
            for node in graph.keys():
                if node not in visited:
                    src = node
                    break
            path = set()
            is_cycle_check = [False]
            self.func_cycle_check(graph, is_cycle_check, src, visited, path)
            if is_cycle_check[0] == True:
                return []
        
        top_sort = []
        visited = set()
        while len(visited) < numCourses:
            for node in graph.keys():
                if node not in visited:
                    src = node
                    break
            len_visited_pre = len(visited)
            self.dfspostorder(src, graph, visited, top_sort)
            len_visited_post = len(visited)
            if len_visited_post == len_visited_pre:
                break
        
        if len(visited) < numCourses:
            return []
        elif len(visited) == numCourses:
            top_sort.reverse()
            return top_sort
    
    def func_cycle_check(self, graph, is_cycle_check, node, visited, path):
        if node in path:
            is_cycle_check[0] = True
            return 

        if node in visited:
            return 

        path.add(node)
        for child in graph[node]:
            self.func_cycle_check(graph, is_cycle_check, child, visited, path)
        path.remove(node)
        visited.add(node)

    
    def dfspostorder(self, node, graph, visited, top_sort):
        for child in graph[node]:
            if child not in visited:
                self.dfspostorder(child, graph, visited, top_sort)
        visited.add(node)
        top_sort.append(node)

        