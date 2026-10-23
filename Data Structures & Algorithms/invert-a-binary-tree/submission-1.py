# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        self.recursion(root)
        return root
    
    def recursion(self, node):
        if node.left is not None or node.right is not None:
            node.left, node.right = node.right, node.left
            if node.left is not None:
                self.recursion(node.left)
            if node.right is not None:
                self.recursion(node.right)