class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        shortest_paths = {}
        for node in range(1, n + 1):
            graph[node] = []
            shortest_paths[node] = float("inf")
        for edge in times:
            src, dest, wt = edge[0], edge[1], edge[2]
            graph[src].append([dest, wt])
        
        p_queue = []
        self.push_to_pqueue((k, 0), p_queue)
        visited = set()
        while len(p_queue) > 0:
            popped_ele = self.pop_from_pqueue(p_queue)
            node, cost = popped_ele[0], popped_ele[1]

            if cost < shortest_paths[node]:
                shortest_paths[node] = cost 

                for childnode in graph[node]:
                    childnode_dst, childnode_wt = childnode[0], childnode[1]
                    self.push_to_pqueue((childnode_dst, cost + childnode_wt), p_queue)

                visited.add(node)
        print("SPs = ", shortest_paths)
        maxdist = float("-inf")
        for node in shortest_paths.keys():
            if shortest_paths[node] > maxdist:
                maxdist = shortest_paths[node]
        return maxdist if maxdist != float("inf") else -1

    def push_to_pqueue(self, node, p_queue):
        p_queue.append(node)
        self.siftUp(p_queue, len(p_queue) - 1)
    
    def siftUp(self, p_queue, idx):
        p_idx = (idx - 1) // 2
        while p_idx >= 0:
            if p_queue[idx][1] < p_queue[p_idx][1]:
                p_queue[idx], p_queue[p_idx] = p_queue[p_idx], p_queue[idx]
                idx = p_idx
                p_idx = (p_idx - 1) // 2
            else:
                break

    def pop_from_pqueue(self, p_queue):
        p_queue[0], p_queue[len(p_queue) - 1] = p_queue[len(p_queue) - 1], p_queue[0]
        popped_ele = p_queue.pop()
        self.siftDown(0, len(p_queue) - 1, p_queue)
        return popped_ele
    
    def siftDown(self, idx, endidx, p_queue):
        c_idx_1 = (2*idx) + 1
        c_idx_2 = (2*idx) + 2
        min_idx = idx
        if c_idx_1 <= endidx:
            if p_queue[c_idx_1][1] < p_queue[min_idx][1]:
                min_idx = c_idx_1
        if c_idx_2 <= endidx:
            if p_queue[c_idx_2][1] < p_queue[min_idx][1]:
                min_idx = c_idx_2
        if idx != min_idx:
            p_queue[min_idx], p_queue[idx] = p_queue[idx], p_queue[min_idx]
            self.siftDown(min_idx, endidx, p_queue)
    


        
        