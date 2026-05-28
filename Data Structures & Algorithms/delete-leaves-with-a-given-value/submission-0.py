# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        boolval = self.helper(root, target)
        if boolval == True:
            return None
        else:
            return root
    
    def helper(self, node, target):

        if node.left is not None:
            isdelleftnode = self.helper(node.left, target)
            if isdelleftnode == True:
                node.left = None
        
        if node.right is not None:
            isdelrightnode = self.helper(node.right, target)
            if isdelrightnode == True:
                node.right = None
        
        if node.left is None and node.right is None and node.val == target:
            return True 
        else:
            return False 