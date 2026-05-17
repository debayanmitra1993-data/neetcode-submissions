# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is not None and q is None:
            return False 
        elif p is None and q is not None:
            return False
        elif p is not None and q is not None:
            return Solution.helper(p, q)
    
    @staticmethod
    def helper(pointer1, pointer2):
        if pointer1.val != pointer2.val:
            return False 
        elif pointer1.val == pointer2.val:
            if pointer1.left is not None:
                if pointer2.left is not None:
                    leftsubtreebool = Solution.helper(pointer1.left, pointer2.left)
                else:
                    return False 
            elif pointer1.left is None:
                if pointer2.left is None:
                    leftsubtreebool = True 
                else:
                    return False  
            
            if pointer1.right is not None:
                if pointer2.right is not None:
                    rightsubtreebool = Solution.helper(pointer1.right, pointer2.right)
                else:
                    return False 
            elif pointer1.right is None:
                if pointer2.right is None:
                    rightsubtreebool = True 
                else:
                    return False  
            
            return leftsubtreebool and rightsubtreebool



