# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path = []
        p_path = []
        q_path = []
        self.dfsbacktrack(root, path, p_path, q_path)
        p_idx, q_idx = 0, 0
        common_node = root
        
        while p_idx < len(p_path) and q_idx < len(q_path):
            if p_path[p_idx] == q_path[q_idx]:
                common_node = p_path[p_idx]
                p_idx += 1
                q_idx += 1
            else:
                return common_node
        return common_node
    
    def dfsbacktrack(self, node, path, p_path, q_path):
        path.append(node)
        if node == p:
            p_path.extend(path.copy())
        if node == q:
            q_path.extend(path.copy())
        
        if node.left is not None:
            self.dfsbacktrack(node.left, path, p_path, q_path)
        if node.right is not None:
            self.dfsbacktrack(node.right, path, p_path, q_path)
        path.pop()


        