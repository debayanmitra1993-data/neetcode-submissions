class Graph:
    
    def __init__(self):
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = []
        if dst not in self.adj_list:
            self.adj_list[dst] = []
        self.adj_list[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list:
            return False 
        else:
            for idx in range(len(self.adj_list[src])):
                ele = self.adj_list[src][idx]
                if ele == dst:
                    self.adj_list[src].pop(idx)
                    return True 
            return False

    def hasPath(self, src: int, dst: int) -> bool:
        return self.bfshelper(src, dst)
        fc = self.dfshelper(src, dst, src, set())
        if fc > 0:
            return True 
        else:
            return False 
    
    def bfshelper(self, src, dst):
        bfsqueue = [src]
        visited = set()

        while len(bfsqueue) > 0:

            ele = bfsqueue.pop(0)
            if ele == dst:
                return True 
            
            if ele in visited:
                continue 
            else:
                visited.add(ele)
            
            for child_node in self.adj_list[ele]:
                bfsqueue.append(child_node)

        return False

        
    def dfshelper(self, src, dst, node, visited):
        if node == dst:
            return 1 
        
        if node in visited:
            return 0
        
        if node == src:
            return 0
        
        visited.add(node)
        count_paths = 0
        for child_node in self.adj_list[node]:
            count_paths += self.dfshelper(src, dst, child_node, visited)
        visited.remove(node)

        return count_paths