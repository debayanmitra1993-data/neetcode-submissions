# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_ancestors = []
        q_ancestors = []
        curr_path = []                                    
        self.dfs(root, p_ancestors, q_ancestors, p, q, curr_path)
        print("p_ancestors = ", p_ancestors)
        print("q_ancestors = ", q_ancestors)
        idx = 0
        lca_idx = 0
        while True:
            if p_ancestors[idx] == q_ancestors[idx]:
                lca_idx = idx
            else:
                break
            
            if (idx + 1) <= len(p_ancestors) - 1 and (idx + 1) <= len(q_ancestors):
                idx += 1 
            else:
                break 
        return p_ancestors[lca_idx]
    
    def dfs(self, node, p_ancestors, q_ancestors, p, q, curr_path):

        curr_path.append(node)
        if node == p:
            p_ancestors.extend(curr_path.copy())
        if node == q:
            q_ancestors.extend(curr_path.copy())



        if node.left is not None:
            self.dfs(node.left, p_ancestors, q_ancestors, p, q, curr_path)
        if node.right is not None:
            self.dfs(node.right, p_ancestors, q_ancestors, p, q, curr_path)
        curr_path.pop()


        
        