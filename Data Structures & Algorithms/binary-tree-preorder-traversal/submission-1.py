# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        out = []
        self.recursion(root, out)
        return out

    def recursion(self, node, out):
        out.append(node.val)
        if node.left is not None:
            self.recursion(node.left, out)
        if node.right is not None:
            self.recursion(node.right, out)

        