# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False 
            
        slowpointer = head 
        fastpointer = head 

        while fastpointer.next is not None:
            
            if fastpointer.next is not None:
                fastpointer = fastpointer.next.next
                if fastpointer is None:
                    break 
            else:
                break 
            slowpointer = slowpointer.next 

            if fastpointer == slowpointer:
                return True 

        return False 
        