# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # generate postorder array
        postorder = []
        if root is not None:
            self.funcpostorderhelper(root, postorder)
        print("postorder = ", postorder)

        count_found = 0
        answernode = None 
        leastdiff = float("inf")
        minval = min(p.val, q.val)
        maxval = max(p.val, q.val)
        for node in postorder:
            if count_found != 2:
                if node.val == p.val or node.val == q.val:
                    count_found += 1 
                    if count_found == 1:
                        comparenode = node 
                    if count_found == 2:
                        ifnotfound = node
            else:
                if node.val >= minval and node.val <= maxval:
                    if abs(comparenode.val - node.val) < leastdiff:
                        leastdiff = abs(comparenode.val - node.val)
                        answernode = node 
        if answernode is not None:
            return answernode
        else:
            return ifnotfound




            

    def funcpostorderhelper(self, node, postorder):
        if node.left is not None:
            self.funcpostorderhelper(node.left, postorder)
        if node.right is not None:
            self.funcpostorderhelper(node.right, postorder)
        postorder.append(node)


        