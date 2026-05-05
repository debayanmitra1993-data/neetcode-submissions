# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevpointer = head
        if prevpointer is None:
            return head
        if prevpointer.next is None:
            return head 
        else:
            currentpointer = prevpointer.next
        
        prevpointer.next = None 

        if currentpointer.next is None:
            currentpointer.next = prevpointer
            prevpointer.next = None 
            return currentpointer 
        else:
            nextpointer = currentpointer.next 


        while currentpointer is not None:
            currentpointer.next = prevpointer

            prevpointer = currentpointer 
            currentpointer = nextpointer
            
            if nextpointer is not None:
                nextpointer = nextpointer.next
            else:
                break
        
        return prevpointer 

             
                              
        
        