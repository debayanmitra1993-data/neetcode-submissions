# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        self.traverse(root, val)
        return root
    
    def traverse(self, node, val):
        if val > node.val:
            if node.right is not None:
                self.traverse(node.right, val)
            else:
                node.right = TreeNode(val)
        elif val < node.val:
            if node.left is not None:
                self.traverse(node.left, val)
            else:
                node.left = TreeNode(val)
