# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        lst = []
        self.inorderhelper(root, lst)
        return lst
    
    def inorderhelper(self, node, arr):
        if node.left is not None:
            self.inorderhelper(node.left, arr)
        arr.append(node.val)
        if node.right is not None:
            self.inorderhelper(node.right, arr)



        