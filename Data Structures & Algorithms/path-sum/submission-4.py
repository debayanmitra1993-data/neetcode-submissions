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
        boolchk = [False]
        self.dfsrecursion(root, boolchk, targetSum, 0)
        return boolchk[0]
    
    def dfsrecursion(self, node, boolchk, targetSum, runsum):
        if node.left is None and node.right is None:
            if node.val + runsum == targetSum:
                boolchk[0] = True
        
        if boolchk[0] == True:
            return 

        if node.left is not None:
            self.dfsrecursion(node.left, boolchk, targetSum, runsum + node.val)
        if node.right is not None:
            self.dfsrecursion(node.right, boolchk, targetSum, runsum + node.val)



        