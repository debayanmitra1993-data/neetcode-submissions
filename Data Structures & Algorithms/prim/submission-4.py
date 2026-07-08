class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for node in range(n):
            graph[node] = []
        for edge in edges:
            src, dest, wt = edge[0], edge[1], edge[2]
            graph[src].append([dest, wt])
            graph[dest].append([src, wt])
        mstval = 0

        # check for connectivity of graph
        visited = set()
        self.check_connectivity(graph, 0, visited)
        if len(visited) < n:
            return -1
        
        # MST algorithm using Prim's
        visited = set()
        visited.add(0)
        min_heap = []
        for childnode in graph[0]:
            dest, wt = childnode[0], childnode[1]
            self.push_to_minheap([0, dest, wt], min_heap)

        mstval = 0
        while len(min_heap) > 0:
            popped_ele = self.pop_from_minheap(min_heap)
            src, dest, wt = popped_ele[0], popped_ele[1], popped_ele[2]
            if dest not in visited:
                visited.add(dest)
                mstval += wt
                for childnode in graph[dest]:
                    child_dest, child_wt = childnode[0], childnode[1]
                    if child_dest not in visited:
                        self.push_to_minheap([dest, child_dest, child_wt], min_heap)
        return mstval

    def push_to_minheap(self, ele, min_heap):
        if len(min_heap) == 0:
            min_heap.append(ele)
            return 
        min_heap.append(ele)
        self.siftUp(min_heap, len(min_heap) - 1)
    
    def siftUp(self, min_heap, idx):
        p_idx = (idx - 1) // 2
        while p_idx >= 0:
            if min_heap[idx][2] < min_heap[p_idx][2]:
                min_heap[idx], min_heap[p_idx] = min_heap[p_idx], min_heap[idx]
                idx = p_idx 
                p_idx = (p_idx - 1) // 2 
            else:
                break

    def pop_from_minheap(self, min_heap):
        min_heap[0], min_heap[len(min_heap) - 1] = min_heap[len(min_heap) - 1], min_heap[0]
        popped_ele = min_heap.pop()
        self.siftDown(min_heap, 0, len(min_heap) - 1)
        return popped_ele
    
    def siftDown(self, min_heap, idx, endidx):
        child_idx_1 = (2*idx) + 1
        child_idx_2 = (2*idx) + 2
        min_idx = idx
        if child_idx_1 <= endidx:
            if min_heap[child_idx_1][2] < min_heap[min_idx][2]:
                min_idx = child_idx_1
        if child_idx_2 <= endidx:
            if min_heap[child_idx_2][2] < min_heap[min_idx][2]:
                min_idx = child_idx_2
        if idx != min_idx:
            min_heap[idx], min_heap[min_idx] = min_heap[min_idx], min_heap[idx]
            self.siftDown(min_heap, min_idx, endidx)
            
    

    def check_connectivity(self, graph, node, visited):
        visited.add(node)
        for childnode in graph[node]:
            dest_node, wt = childnode[0], childnode[1]
            if dest_node not in visited:
                self.check_connectivity(graph, dest_node, visited)
        

        



        