# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        root_inc, root_exc = self.postordertraversal(root)
        return max(root_inc, root_exc)

    def postordertraversal(self, node):
        if node.left is not None:
            left_inc, left_exc = self.postordertraversal(node.left)
        else:
            left_inc, left_exc = 0, 0

        if node.right is not None:
            right_inc, right_exc = self.postordertraversal(node.right)
        else:
            right_inc, right_exc = 0, 0
        
        inc = node.val + left_exc + right_exc
        exc = max(left_inc, left_exc) + max(right_inc, right_exc)

        return inc, exc
        


        