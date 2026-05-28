class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) == 0:
            return 0
        
        graph = {}
        for node in range(n):
            graph[node] = []

        edgewts = {}
        for edge in edges:
            src, dest, wt = edge[0], edge[1], edge[2]
            edgewts[str(src) + "_" + str(dest)] = wt
            edgewts[str(dest) + "_" + str(src)] = wt
            if src not in graph:
                graph[src] = []
            if dest not in graph:
                graph[dest] = []
            graph[src].append(dest)
            graph[dest].append(src)
        
        # check whether graph is connected, if not connected, return -1
        is_graph_connected = self.check_graph_connected(graph)
        if is_graph_connected == False:
            return -1

        visited = set()
        src_node = edges[0][0]
        visited.add(src_node)
        min_heap = []
        for connected_node in graph[src_node]:
            edge = str(src_node) + "_" + str(connected_node)
            edge_wt = edgewts[edge]
            self.push_to_min_heap([src_node, connected_node, edge_wt], min_heap)

        mst_sum = 0

        while len(min_heap) > 0:
            edge_popped = self.pop_from_min_heap(min_heap)
            dest_node = edge_popped[1]
            edge_weight = edge_popped[2]
            if dest_node in visited:
                continue
            visited.add(dest_node)
            mst_sum += edge_weight

            for child_node in graph[dest_node]:
                if child_node not in visited:
                    edge = str(dest_node) + "_" + str(child_node)
                    edge_wt = edgewts[edge]
                    self.push_to_min_heap([dest_node, child_node, edge_wt], min_heap)
        return mst_sum 

    def pop_from_min_heap(self, min_heap):
        min_heap[0], min_heap[len(min_heap) - 1] = min_heap[len(min_heap) - 1], min_heap[0]
        catch_ele = min_heap.pop()
        self.siftDown(0, len(min_heap) - 1, min_heap)
        return catch_ele
        
    def push_to_min_heap(self, edge, min_heap):
        if len(min_heap) == 0:
            min_heap.append(edge)
            return
        min_heap.append(edge)
        min_heap = self.siftUp(min_heap, len(min_heap) - 1)
    
    def siftDown(self, idx, endidx, min_heap):
        child_idx_1 = (2*idx) + 1
        child_idx_2 = (2*idx) + 2
        min_idx = idx
        if child_idx_1 <= endidx:
            if min_heap[child_idx_1][2] < min_heap[idx][2]:
                min_idx = child_idx_1
        if child_idx_2 <= endidx:
            if min_heap[child_idx_2][2] < min_heap[min_idx][2]:
                min_idx = child_idx_2
        if min_idx != idx:
            min_heap[idx], min_heap[min_idx] = min_heap[min_idx], min_heap[idx]
            self.siftDown(min_idx, endidx, min_heap)

    def siftUp(self, min_heap, idx):
        p_idx = (idx - 1) // 2
        while p_idx >= 0:
            p_edge = min_heap[p_idx]
            c_edge = min_heap[idx]
            p_edge_wt = p_edge[2]
            c_edge_wt = c_edge[2]
            if p_edge_wt > c_edge_wt:
                min_heap[p_idx], min_heap[idx] = min_heap[idx], min_heap[p_idx]
                idx = p_idx
                p_idx = (p_idx - 1) // 2
            else:
                break
        return min_heap
    
    def check_graph_connected(self, graph):
        print("graph = ", graph)
        visited = set()
        for srcnode in graph.keys():
            dfsstack = [srcnode]
            # print("dfsstack = ", dfsstack)
            break

        while len(dfsstack) > 0:
            ele = dfsstack.pop()
            if ele in visited:
                continue
            
            visited.add(ele)
            print("visited = ", visited)
            for childnode in graph[ele]:
                if childnode not in visited:
                    dfsstack.append(childnode)

        return len(visited) == len(graph.keys())