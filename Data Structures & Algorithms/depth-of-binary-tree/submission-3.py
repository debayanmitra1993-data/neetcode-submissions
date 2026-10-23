# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxd = [1]
        self.recursion(root, 1, maxd)
        return maxd[0]
    
    def recursion(self, node, depth, maxd):
        if depth > maxd[0]:
            maxd[0] = depth
        
        if node.left is not None:
            self.recursion(node.left, depth + 1, maxd)
        if node.right is not None:
            self.recursion(node.right, depth + 1, maxd)
        


        