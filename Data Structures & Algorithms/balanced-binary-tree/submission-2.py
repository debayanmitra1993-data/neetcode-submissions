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
        sol = [True]
        self.helper(root, sol)
        print("sol = ", sol)
        return sol[0]
    
    def helper(self, node, sol):
        if node.left is None:
            lst_dep = 0
        else:
            lst_dep = self.helper(node.left, sol) + 1
        
        if node.right is None:
            rst_dep = 0 
        else:
            rst_dep = self.helper(node.right, sol) + 1
        
        dep = max(lst_dep, rst_dep)

        if abs(lst_dep - rst_dep) > 1:
            sol[0] = False 
        
        return dep