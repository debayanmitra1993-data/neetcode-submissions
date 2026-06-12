# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sp = head
        fp = head 

        while fp.next is not None:

            if sp.next is not None:
                sp = sp.next 
            
            if fp.next.next is not None:
                fp = fp.next.next 
            elif fp.next.next is None:
                if fp.next is not None:
                    fp = fp.next 
                elif fp.next is None:
                    break
        return sp

        