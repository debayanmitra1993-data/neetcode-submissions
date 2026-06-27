# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst = []
        pointer = head
        while pointer is not None:
            lst.append(pointer.val)
            pointer = pointer.next 
        
        i = 0
        j = len(lst) - 1 
        maxtwinsum = float("-inf")
        while i < j:
            if lst[i] + lst[j] > maxtwinsum:
                maxtwinsum = lst[i] + lst[j]
            i += 1
            j -= 1 
        return maxtwinsum


        