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
        
        branchdepths = []
        Solution.helper(root, 1, branchdepths)
        return max(branchdepths)

    @staticmethod
    def helper(node, currentdepth, branchdepths):
        if node.left is None and node.right is None:
            branchdepths.append(currentdepth) 
        else:
            if node.left is not None:
                Solution.helper(node.left, currentdepth + 1, branchdepths)
            if node.right is not None:
                Solution.helper(node.right, currentdepth + 1, branchdepths)
        



        