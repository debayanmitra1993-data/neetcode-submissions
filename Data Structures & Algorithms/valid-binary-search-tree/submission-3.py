# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        boolval = [True]
        self.recursion(root, float("-inf"), float("inf"), boolval)
        return boolval[0]
    
    def recursion(self, node, minallowed, maxallowed, boolval):
        if boolval[0] == False:
            return 
        
        if not (node.val > minallowed and node.val < maxallowed):
            boolval[0] = False
            return 
        
        if node.left is not None:
            self.recursion(node.left, minallowed, node.val, boolval)
        
        if node.right is not None:
            self.recursion(node.right, node.val, maxallowed, boolval)


