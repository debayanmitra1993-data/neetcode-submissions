"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        visited = set()
        graph = {}
        self.dfs(node, visited, graph)

        # Dictionary to store cloned nodes
        clone_map = {}
        clone_map[node.val] = Node(node.val)

        visited = set()
        self.construct_graph(clone_map[node.val], graph, visited, clone_map)

        return clone_map[node.val]

    def construct_graph(self, node, graph, visited, clone_map):
        visited.add(node.val)

        for childnodeval in graph[node.val]:

            # Create child only once
            if childnodeval not in clone_map:
                clone_map[childnodeval] = Node(childnodeval)

            childnode = clone_map[childnodeval]

            # Add edge
            node.neighbors.append(childnode)

            # DFS
            if childnodeval not in visited:
                self.construct_graph(childnode, graph, visited, clone_map)

    def dfs(self, node, visited, graph):
        visited.add(node.val)

        if node.val not in graph:
            graph[node.val] = []

        for childnode in node.neighbors:
            graph[node.val].append(childnode.val)

            if childnode.val not in visited:
                self.dfs(childnode, visited, graph)