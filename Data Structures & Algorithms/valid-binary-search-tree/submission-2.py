# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        boollst = [True]
        self.recursionhelper(root, float("-inf"), float("inf"), boollst)
        return boollst[0]
    
    def recursionhelper(self, node, minallowed, maxallowed, boollst):
        if not (node.val > minallowed and node.val < maxallowed):
            boollst[0] = False
            return
        
        if node.left is not None:
            self.recursionhelper(node.left, minallowed, node.val, boollst)
        if node.right is not None:
            self.recursionhelper(node.right, node.val, maxallowed, boollst)
        

        


        