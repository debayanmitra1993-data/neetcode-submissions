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
        return Solution.funchelper(root, 0, targetSum)
    
    @staticmethod
    def funchelper(node, runsum, targetSum):
        runsum += node.val

        if node.left is None and node.right is None:
            if runsum == targetSum:
                return True
            else:
                return False 
        
        hasleftpathsum = False
        if node.left is not None:
            hasleftpathsum = Solution.funchelper(node.left, runsum, targetSum)
        
        hasrightpathsum = False
        if node.right is not None:
            hasrightpathsum = Solution.funchelper(node.right, runsum, targetSum)
        
        return hasleftpathsum or hasrightpathsum


