class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # construct graph (adj list)
        graph = {}
        for node in range(1, n + 1):
            graph[node] = []
        for src, dest in trust:
            graph[src].append(dest)
        
        # check if any of the node has 0 child nodes...
        zero_child_node = [k for k,v in graph.items() if len(v) == 0]

        if len(zero_child_node) == 0:
            return -1
        else:
            for node in graph.keys():
                if node != zero_child_node[0]:
                    if zero_child_node[0] not in graph[node]:
                        return -1
            return zero_child_node[0]