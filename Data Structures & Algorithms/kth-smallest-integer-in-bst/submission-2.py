# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kval = [0]
        ans = [0]
        self.inordertraverse(root, k, kval, ans)
        return ans[0]

    def inordertraverse(self, node, k, kval, ans):
        if node.left is not None:
            self.inordertraverse(node.left, k, kval, ans)
        
        # here..
        kval[0] = kval[0] + 1
        if kval[0] == k:
            ans[0] = node.val
        
        # if answer is found, break out of loop...
        if kval[0] == k:
            return 
        
        if node.right is not None:
            self.inordertraverse(node.right, k, kval, ans)

        