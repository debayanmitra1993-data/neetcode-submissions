# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxdialst = [float("-inf")]
        _ = self.recursiontree(root, maxdialst)
        return maxdialst[0]
    
    def recursiontree(self, node, maxdialst):
        if node.left is not None:
            lstheight = self.recursiontree(node.left, maxdialst)
        else:
            lstheight = 0
    
        if node.right is not None:
            rstheight = self.recursiontree(node.right, maxdialst)
        else:
            rstheight = 0
    
        if lstheight + rstheight > maxdialst[0]:
            maxdialst[0] = lstheight + rstheight
            print("putting value = ", maxdialst[0])
    
        return 1 + max(lstheight, rstheight)