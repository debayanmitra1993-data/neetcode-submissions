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
        self.inserthelper(root, val)
        return root
    
    def inserthelper(self, node, val):
        if val > node.val:
            # insert right 
            if node.right is not None:
                self.inserthelper(node.right, val)
            else:
                node.right = TreeNode(val)
        else:
            # insert left 
            if node.left is not None:
                self.inserthelper(node.left, val)
            else:
                node.left = TreeNode(val)
        