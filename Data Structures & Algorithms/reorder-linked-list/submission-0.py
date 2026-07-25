# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arrstore = []
        pointer = head
        while pointer is not None:
            arrstore.append(pointer.val)
            pointer = pointer.next 
        
        i = 0
        j = len(arrstore) - 1
        
        pointer = head

        while i <= j:
            if i > 0:
                newnode = ListNode(arrstore[i])
                pointer.next = newnode 
                pointer = newnode 
            
            if j != i:
                newnode = ListNode(arrstore[j])
                pointer.next = newnode
                pointer = newnode
            else:
                break
            
            i += 1 
            j -= 1
        


            
            





        