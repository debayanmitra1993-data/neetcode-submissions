# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        carryover = 0
        newp = ListNode()
        newphead = newp

        while (p1 is not None) or (p2 is not None) or (carryover > 0):

            newpval = carryover
            if p1 is not None:
                newpval += p1.val
            if p2 is not None:
                newpval += p2.val 
            # print("newpval = ", newpval)
            
            if newpval >= 10:
                newp.val = newpval % 10 
                carryover = newpval // 10
            else:
                newp.val = newpval 
                carryover = 0
            # print("carryover = ", carryover)
            # print(newp.val)
            
            if p1 is not None:
                if p1.next is not None:
                    p1 = p1.next 
                else:
                    p1 = None 
            # print("p1 = ", p1)
            
            if p2 is not None:
                if p2.next is not None:
                    p2 = p2.next 
                else:
                    p2 = None 
            # print("p2 = ", p2)
            
            if p1 is not None or p2 is not None or carryover > 0:
                newp.next = ListNode()
                newp = newp.next
        return newphead

            

