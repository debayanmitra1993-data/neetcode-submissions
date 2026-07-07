class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = {}
        shortest_paths = {}
        for node in range(n):
            graph[node] = []
            shortest_paths[node] = float("inf")
        for edge in edges:
            start, end, wt = edge[0], edge[1], edge[2]
            graph[start].append([end, wt])
        
        min_heap = [[0, src]]
        visited = set()

        while len(min_heap) > 0:
            popped_ele = self.pop_from_minheap(min_heap)
            cost, node = popped_ele[0], popped_ele[1]
            if cost < shortest_paths[node]:
                shortest_paths[node] = cost 

                for childnode in graph[node]:
                    dest, wt = childnode[0], childnode[1]
                    self.push_to_minheap([cost + wt, dest], min_heap)
                
                visited.add(node)
        
        print("shortest paths = ", shortest_paths)
        for node in shortest_paths.keys():
            if shortest_paths[node] == float("inf"):
                shortest_paths[node] = -1
        return shortest_paths
        
        
    
    def pop_from_minheap(self, min_heap):
        min_heap[0], min_heap[len(min_heap) - 1] = min_heap[len(min_heap) - 1], min_heap[0]
        ele_to_pop = min_heap.pop()

        self.siftDown(0, min_heap, len(min_heap) - 1)
        return ele_to_pop
        

    def siftDown(self, idx, min_heap, endidx):
        child_idx_1 = (2*idx) + 1
        child_idx_2 = (2*idx) + 2
        min_idx = idx
        if child_idx_1 <= endidx:
            if min_heap[child_idx_1][0] < min_heap[min_idx][0]:
                min_idx = child_idx_1
        if child_idx_2 <= endidx:
            if min_heap[child_idx_2][0] < min_heap[min_idx][0]:
                min_idx = child_idx_2
        if min_idx != idx:
            min_heap[idx], min_heap[min_idx] = min_heap[min_idx], min_heap[idx]
            self.siftDown(min_idx, min_heap, endidx)

    def push_to_minheap(self, ele, min_heap):
        if len(min_heap) == 0:
            min_heap.append(ele)
            return 
        min_heap.append(ele)
        self.siftUp(min_heap, len(min_heap) - 1)
    
    def siftUp(self, min_heap, idx):
        p_idx = (idx - 1) // 2 
        while p_idx >= 0:
            if min_heap[idx][0] < min_heap[p_idx][0]:
                min_heap[idx], min_heap[p_idx] = min_heap[p_idx], min_heap[idx]
                idx = p_idx 
                p_idx = (idx - 1) // 2
            else:
                break





            

             
            
            

        
         

