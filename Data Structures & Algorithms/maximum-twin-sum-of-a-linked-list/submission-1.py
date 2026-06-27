# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slowpointer = head
        fastpointer = head 

        while fastpointer is not None:
            slowpointer = slowpointer.next 
            fastpointer = fastpointer.next.next 
        
        if slowpointer.next is None:
            return head.val + head.next.val
        
        prevpointer = slowpointer
        currpointer = prevpointer.next
        nextpointer = currpointer.next
        
        prevpointer.next = None 
        while nextpointer is not None:
            currpointer.next = prevpointer 

            prevpointer = currpointer 
            currpointer = nextpointer
            nextpointer = nextpointer.next 
        currpointer.next = prevpointer 
        tail = currpointer 

        leftpointer = head
        rightpointer = tail
        maxvalsofar = float("-inf")

        while True:
            if leftpointer.val + rightpointer.val > maxvalsofar:
                maxvalsofar = leftpointer.val + rightpointer.val
            leftpointer = leftpointer.next
            rightpointer = rightpointer.next 

            if leftpointer == slowpointer:
                break
        
        return maxvalsofar



        