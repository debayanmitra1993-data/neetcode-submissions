# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        bfsq = deque()
        if root is None:
            return []
        
        bfsq.append((root, 1)) # (node, depth)..
        bfs_out = {} # (height : [ele1, ele2...])

        while len(bfsq) > 0:
            node, depth = bfsq.popleft()
            if depth not in bfs_out:
                bfs_out[depth] = []
            bfs_out[depth].append(node.val)

            if node.left is not None:
                bfsq.append((node.left, depth + 1))
            if node.right is not None:
                bfsq.append((node.right, depth + 1))
        
        out = []
        for depth in bfs_out.keys():
            out.append(bfs_out[depth])
        return out




        