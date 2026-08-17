# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        outstore = {}
        bfsqueue = deque()
        bfsqueue.append((1, root))
        while len(bfsqueue) > 0:
            popped = bfsqueue.popleft()
            depth, node = popped[0], popped[1]
            if depth not in outstore:
                outstore[depth] = []
            outstore[depth].append(node.val)

            if node.left is not None:
                bfsqueue.append((depth + 1, node.left))
            if node.right is not None:
                bfsqueue.append((depth + 1, node.right))
        
        return [x[1][-1] for x in outstore.items()]
        
        