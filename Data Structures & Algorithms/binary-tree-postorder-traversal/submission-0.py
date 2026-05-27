# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        lst = []
        self.postorderhelper(root, lst)
        return lst
    
    def postorderhelper(self, node, arr):
        if node.left is not None:
            self.postorderhelper(node.left, arr)
        
        if node.right is not None:
            self.postorderhelper(node.right, arr)
        arr.append(node.val)
        