# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        outstr = ""
        pointer = root 
        outstr = self.serialization(pointer)
        print("outstr = ", outstr)
        return outstr
    
    def serialization(self, pointer):
        mystr = str(pointer.val) + ","
        
        if pointer.left is None:
            mystr += "N,"
        else:
            mystr += self.serialization(pointer.left)
        
        if pointer.right is None:
            mystr += "N,"
        else:
            mystr += self.serialization(pointer.right)
        
        return mystr
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        
        data_lst = data.split(",")
        # rootnode = TreeNode(int(data[0]))
        # currpointer = rootnode
        return self.deserialization(data_lst, [0])
        # return rootnode 

    def deserialization(self, data_lst, curridx_lst):
        curridx = curridx_lst[0]
        if curridx > len(data_lst) - 1:
            return None
        
        if data_lst[curridx] == "N":
            curridx += 1 
            curridx_lst[0] = curridx
            return None 
        elif data_lst[curridx] != "N":
            node = TreeNode(int(data_lst[curridx]))
            curridx += 1 
            curridx_lst[0] = curridx
            node.left = self.deserialization(data_lst, curridx_lst)
            node.right = self.deserialization(data_lst, curridx_lst)
            return node
