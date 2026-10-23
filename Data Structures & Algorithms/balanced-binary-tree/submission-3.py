# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        boolchk = [True]
        self.recursion(root, boolchk)
        return boolchk[0]

    def recursion(self, node, boolchk):
        if node.left is not None:
            lstheight = self.recursion(node.left, boolchk)
        else:
            lstheight = 0
        
        if node.right is not None:
            rstheight = self.recursion(node.right, boolchk)
        else:
            rstheight = 0
        
        if abs(lstheight - rstheight) > 1:
            boolchk[0] = False
        
        return max(lstheight, rstheight) + 1

        