class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = {}
        shortest_path = {}
        start_node = src

        for node in range(n):
            graph[node] = []
            shortest_path[node] = float("inf")

        for edge in edges:
            src, dest, wt = edge[0], edge[1], edge[2]
            if src not in graph:
                graph[src] = []
            if dest not in graph:
                graph[dest] = []
            graph[src].append([dest, wt])
        print("graph = ", graph)

        src = start_node
        shortest_path[src] = 0
        minheap = [[src, shortest_path[src]]]
        visited_nodes = set()

        while len(minheap) > 0:
            popped_node = self.pop_from_minheap(minheap)
            print("popped_node = ", popped_node)
            src = popped_node[0]
            if src in visited_nodes:
                continue

            for child in graph[src]:
                dest = child[0]
                wt = child[1]
                if dest not in visited_nodes:
                    if shortest_path[src] + wt < shortest_path[dest]:
                        shortest_path[dest] = shortest_path[src] + wt
                        self.push_to_minheap([dest, shortest_path[dest]], minheap)
            
            visited_nodes.add(src)
        
        print("shortest_path = ", shortest_path)
        for node in shortest_path.keys():
            if shortest_path[node] == float("inf"):
                shortest_path[node] = -1
        return shortest_path
    
    def pop_from_minheap(self, minheap):
        minheap[0], minheap[len(minheap) - 1] = minheap[len(minheap) - 1], minheap[0]
        ele = minheap.pop()
        if len(minheap) > 0:
            self.siftDown(0, minheap, len(minheap) - 1)
        return ele

    def siftDown(self, idx, minheap, endidx):
        child_idx_1 = (2*idx) + 1
        child_idx_2 = (2*idx) + 2
        min_idx = idx
        if child_idx_1 <= endidx:
            if minheap[child_idx_1][1] < minheap[idx][1]:
                min_idx = child_idx_1
        if child_idx_2 <= endidx:
            if minheap[child_idx_2][1] < minheap[min_idx][1]:
                min_idx = child_idx_2
        if idx != min_idx:
            minheap[min_idx], minheap[idx] = minheap[idx], minheap[min_idx]
            self.siftDown(min_idx, minheap, endidx)

    
    def push_to_minheap(self, edge, minheap):
        if len(minheap) == 0:
            minheap.append(edge)
            return
        minheap.append(edge)
        self.siftUp(len(minheap) - 1, minheap)
    
    def siftUp(self, idx, minheap):
        p_idx = (idx - 1) // 2
        while p_idx >= 0:
            p_ele = minheap[p_idx]
            c_ele = minheap[idx]

            if c_ele[1] < p_ele[1]:
                minheap[p_idx], minheap[idx] = minheap[idx], minheap[p_idx]
                idx = p_idx
                p_idx = (p_idx - 1) // 2
            else:
                break

    


