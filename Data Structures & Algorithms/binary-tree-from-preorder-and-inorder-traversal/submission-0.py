# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder, inorder)

    def build(self, preorder, inorder):
        node = TreeNode(preorder[0])
        inorder_idx = inorder.index(preorder[0])
        
        lst_inorder = inorder[:inorder_idx]
        rst_inorder = inorder[inorder_idx + 1:]
        
        lst_preorder = preorder[1:inorder_idx + 1]
        rst_preorder = preorder[inorder_idx + 1:]

        if len(lst_inorder) > 0:
            node.left = self.build(lst_preorder, lst_inorder)
        if len(rst_inorder) > 0:
            node.right = self.build(rst_preorder, rst_inorder)
        return node

        
        