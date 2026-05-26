# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return 0 
        
        maxval = [float("-inf")]
        self.helper(root, maxval)
        return maxval[0]
    
    def helper(self, node, maxval):
        if node.left is None and node.right is None:
            return 0 
        
        if node.left is not None:
            lst_dep = self.helper(node.left, maxval) + 1
        else:
            lst_dep = 0
        
        if node.right is not None:
            rst_dep = self.helper(node.right, maxval) + 1
        else:
            rst_dep = 0 
        
        depth = max(lst_dep, rst_dep)
        if lst_dep + rst_dep > maxval[0]:
            maxval[0] = lst_dep + rst_dep
        return depth