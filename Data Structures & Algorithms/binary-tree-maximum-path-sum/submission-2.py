# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_nodemax = [float("-inf")]
        self.helper(root, max_nodemax)
        print("max_nodemax = ", max_nodemax)
        return max_nodemax[0]
    
    def helper(self, node, max_nodemax):
        if node.left is not None:
            leftsubmax = self.helper(node.left, max_nodemax)
        else:
            leftsubmax = 0

        if node.right is not None:
            rightsubmax = self.helper(node.right, max_nodemax)
        else:
            rightsubmax = 0
        
        nodemax = max(
            leftsubmax + node.val,
            rightsubmax + node.val,
            node.val
        )

        nodemax_store = max(nodemax, leftsubmax + node.val + rightsubmax)
        
        if nodemax_store > max_nodemax[-1]:
            max_nodemax.pop()
            max_nodemax.append(nodemax_store)
        return nodemax
        