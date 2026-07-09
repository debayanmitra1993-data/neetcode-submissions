class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        for node in range(n):
            graph[node] = []
        for edge in edges:
            src, dest = edge[0], edge[1]
            graph[src].append(dest)
        
        # check if cycle exists in this di-graph
        cycle_lst = [False]
        visited = set()
        path = set()
        boolcheck = self.cycle_check(graph, cycle_lst, visited, path, 0)
        if cycle_lst[0] == True:
            return []
        
        # perform post order DFS..(graph can be connected / un-connected)
        visited = set()
        top_sort = []
        while len(visited) < n:
            # get the starting node..
            for node in range(n):
                if node not in visited:
                    break
            
            self.postorderdfs(node, visited, top_sort, graph)
        
        final_top_sort = [0]*len(top_sort)
        for idx in range(len(top_sort)):
            final_top_sort[len(top_sort) - idx - 1] = top_sort[idx]
        return final_top_sort
    

    def postorderdfs(self, node, visited, top_sort, graph):
        for childnode in graph[node]:
            if childnode not in visited:
                self.postorderdfs(childnode, visited, top_sort, graph)
        visited.add(node)
        top_sort.append(node)
        

        
    
    def cycle_check(self, graph, cycle_lst, visited, path, node):
        if cycle_lst[0] == True:
            return 

        path.add(node)

        for childnode in graph[node]:
            if childnode in path:
                cycle_lst[0] = True
                return 
            if childnode not in visited:
                self.cycle_check(graph, cycle_lst, visited, path, childnode)
        
        visited.add(node)
        path.remove(node)





        