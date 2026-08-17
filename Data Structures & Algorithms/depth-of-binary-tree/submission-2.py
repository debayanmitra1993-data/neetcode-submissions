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
        self.recursion(root, maxd, 1)
        return maxd[0]
    
    def recursion(self, node, maxd, currentdepth):
        if currentdepth > maxd[0]:
            maxd[0] = currentdepth
        
        if node.left is not None:
            self.recursion(node.left, maxd, currentdepth + 1)
        if node.right is not None:
            self.recursion(node.right, maxd, currentdepth + 1)




        