# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        lst = []
        self.helper(root, lst, float("-inf"))
        return len(lst)
    
    def helper(self, node, lst, maxvalbranch):
        if node.val >= maxvalbranch:
            lst.append(node.val)
            maxvalbranch = node.val
        
        if node.left is not None:
            self.helper(node.left, lst, maxvalbranch)
        if node.right is not None:
            self.helper(node.right, lst, maxvalbranch)



        