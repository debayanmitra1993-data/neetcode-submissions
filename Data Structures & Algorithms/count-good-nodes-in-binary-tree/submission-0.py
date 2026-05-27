# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, root.val)
    
    def helper(self, node, maxsofar):
        if node.val >= maxsofar:
            count = 1
        else:
            count = 0

        if node.left is not None:
            lst_count = self.helper(node.left, max(maxsofar, node.val))
        else:
            lst_count = 0
        
        if node.right is not None:
            rst_count = self.helper(node.right, max(maxsofar, node.val))
        else:
            rst_count = 0 
        
        return count + lst_count + rst_count

        