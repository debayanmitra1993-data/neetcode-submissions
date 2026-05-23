# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is not None:
            return self.helper(root, float("-inf"), float("inf"))
    
    def helper(self, node, minval, maxval):
        if node.val > minval and node.val < maxval:
            if node.left is not None:
                lstcorrectbool = self.helper(node.left, minval, node.val)
            else:
                lstcorrectbool = True

            if node.right is not None:
                rstcorrectbool = self.helper(node.right, node.val, maxval)
            else:
                rstcorrectbool = True 

            return lstcorrectbool and rstcorrectbool 
        else:
            return False 

        