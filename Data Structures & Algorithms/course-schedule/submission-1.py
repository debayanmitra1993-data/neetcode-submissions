class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for node in range(numCourses):
            graph[node] = []
        for prereq in prerequisites:
            dest, src = prereq[0], prereq[1]
            if src not in graph:
                graph[src] = []
            if dest not in graph:
                graph[dest] = []
            graph[src].append(dest)
        
        visited = set()
        path = set()
        src = 0
        cycle_bool_lst = [False]
        while len(visited) < numCourses:
            for node in graph:
                if node in visited:
                    continue
                elif node not in visited:
                    src = node
                    break
            
            self.cycle_check(src, visited, path, cycle_bool_lst, graph)
            if cycle_bool_lst[0] == True:
                return False
        
        return len(visited) == numCourses
        
    
    def cycle_check(self, node, visited, path, cycle_bool_lst, graph):
        if node in path:
            cycle_bool_lst[0] = True 
            return 
        
        if node in visited:
            return 
        
        visited.add(node)
        path.add(node)
        for child in graph[node]:
            self.cycle_check(child, visited, path, cycle_bool_lst, graph)
        path.remove(node)
        