# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subrootval = subRoot.val
        bool_lst = []
        Solution.helper(root, subRoot, bool_lst)
        print("bool_lst = ", bool_lst)
        for bool_val in bool_lst:
            if bool_val == True:
                return True 
        return False 

    @staticmethod
    def helper(node, subnode, bool_lst):
        if node.val == subnode.val:
            # call the function for checking
            issubroot = Solution.funcsubrootcheck(node, subnode)
            bool_lst.append(issubroot)
        
        if node.left is not None:
            Solution.helper(node.left, subnode, bool_lst)
        if node.right is not None:
            Solution.helper(node.right, subnode, bool_lst)
    
    @staticmethod
    def funcsubrootcheck(node, subnode):
        if node.val == subnode.val:
            if node.left is not None:
                if subnode.left is not None:
                    isleftvalid = Solution.funcsubrootcheck(node.left, subnode.left)
                else:
                    isleftvalid = False 
            elif node.left is None:
                if subnode.left is None:
                    isleftvalid = True
                else:
                    isleftvalid = False 

            if node.right is not None:
                if subnode.right is not None:
                    isrightvalid = Solution.funcsubrootcheck(node.right, subnode.right)
                else:
                    isrightvalid = False
            elif node.right is None:
                if subnode.right is None:
                    isrightvalid = True 
                else:
                    isrightvalid = False 
            
            return isleftvalid and isrightvalid 
        else:
            return False


        