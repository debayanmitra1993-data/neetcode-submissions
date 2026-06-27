# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None 
        
        if head.next is None:
            return head 
        
        if head.next.next is None:
            pointer = head.next 
            pointer.next = head 
            head.next = None 
            head = pointer 
            return head 
        
        prevpointer = head 
        currpointer = prevpointer.next
        nextpointer = currpointer.next 

        prevpointer.next = None
        while nextpointer is not None:
            currpointer.next = prevpointer 

            prevpointer = currpointer 
            currpointer = nextpointer 
            nextpointer = nextpointer.next 
        
        currpointer.next = prevpointer 
        head = currpointer
        return head 

        
    
        
