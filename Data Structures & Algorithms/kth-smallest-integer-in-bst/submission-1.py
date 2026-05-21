# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        out = []
        self.helper(root, k, out)
        print("out = ", out)
        return out[-1]
    
    def helper(self, node, k, out):
        if node.left is not None:
            chk = self.helper(node.left, k, out)
            if chk == True:
                return True 
        out.append(node.val)
        if len(out) == k:
            return True
        if node.right is not None:
            chk = self.helper(node.right, k, out)
            if chk == True:
                return True 
        
        