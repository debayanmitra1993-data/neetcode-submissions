# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowpointer = head 
        fastpointer = head

        while slowpointer is not None and fastpointer is not None:
            if slowpointer.next is not None:
                slowpointer = slowpointer.next
            else:
                return False
            
            if fastpointer.next is not None:
                if fastpointer.next.next is not None:
                    fastpointer = fastpointer.next.next
                else:
                    return False
            else:
                return False

            if fastpointer == slowpointer:
                return True
        return False