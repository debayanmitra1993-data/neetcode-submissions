# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowpointer = head
        fastpointer = head

        while fastpointer is not None:

            # odd length case...
            if fastpointer.next is None:
                return slowpointer
            
            # even length case...
            if fastpointer.next.next is None:
                return slowpointer.next
            
            slowpointer = slowpointer.next
            fastpointer = fastpointer.next.next
        




        