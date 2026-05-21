# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        mydict = {}
        if root is None:
            return []
        elif root is not None:
            self.helper(root, mydict, 0)
        print("mydict = ", mydict)
        out = []
        for key in mydict.keys():
            out.append(mydict[key])
        return out

    def helper(self, node, mydict, depth):
        if depth not in mydict:
            mydict[depth] = [node.val]
        else:
            mydict[depth].append(node.val)
        
        if node.left is not None:
            self.helper(node.left, mydict, depth + 1)
        if node.right is not None:
            self.helper(node.right, mydict, depth + 1)


        