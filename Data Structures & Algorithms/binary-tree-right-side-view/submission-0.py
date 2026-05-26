# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        b_nodes = {}
        self.helper(root, b_nodes, 0)
        print("b_nodes = ", b_nodes)
        out = []
        for dep in b_nodes.keys():
            catch = b_nodes[dep].pop()
            out.append(catch)
        return out
    
    def helper(self, node, b_nodes, depth):
        bfs_queue = [[node, depth]]

        while len(bfs_queue) > 0:
            ele = bfs_queue.pop(0)
            node = ele[0]
            depth = ele[1]
            
            if depth in b_nodes:
                b_nodes[depth].append(node.val)
            else:
                b_nodes[depth] = [node.val]

            # append children of ele to queue
            if node.left is not None:
                bfs_queue.append([node.left, depth + 1])
            if node.right is not None:
                bfs_queue.append([node.right, depth + 1])




        