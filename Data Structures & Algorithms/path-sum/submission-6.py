# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        boollst = [False]
        self.recursiontree(root, targetSum, 0, boollst)
        return boollst[0]
    
    def recursiontree(self, node, targetSum, runsum, boollst):
        if node.left is None and node.right is None:
            if runsum + node.val == targetSum:
                boollst[0] = True
        
        if node.left is not None:
            self.recursiontree(node.left, targetSum, runsum + node.val, boollst)
        if node.right is not None:
            self.recursiontree(node.right, targetSum, runsum + node.val, boollst)


        