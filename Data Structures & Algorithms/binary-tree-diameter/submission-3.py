# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxd = [0]
        self.recursion(root, maxd)
        return maxd[0]
    
    def recursion(self, node, maxd):
        if node.left is not None:
            lstheight = self.recursion(node.left, maxd)
        else:
            lstheight = 0
        
        if node.right is not None:
            rstheight = self.recursion(node.right, maxd)
        else:
            rstheight = 0
        
        path = lstheight + rstheight
        if path > maxd[0]:
            maxd[0] = path
        
        return max(lstheight, rstheight) + 1 
        