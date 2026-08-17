# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lst = []
        final_p_lst = []
        final_q_lst = []
        self.recursion(root, p, lst, final_p_lst)
        self.recursion(root, q, lst, final_q_lst)
        
        idx = 0
        while idx < len(final_p_lst) and idx < len(final_q_lst):
            if final_p_lst[idx] == final_q_lst[idx]:
                ans = final_p_lst[idx]
                idx += 1
            else:
                break
        return ans

    def recursion(self, node, p, lst, final_p_lst):
        if node.val == p.val:
            lst.append(node)
            final_p_lst.extend(lst.copy())
            lst.pop()
            return  
        if node.left is not None:
            lst.append(node)
            self.recursion(node.left, p, lst, final_p_lst)
        if node.right is not None:
            lst.append(node)
            self.recursion(node.right, p, lst, final_p_lst)
        if len(lst) > 0:
            lst.pop()
        

            

        