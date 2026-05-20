# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer = head
        length_ll = 0
        while pointer is not None: 
            length_ll += 1
            pointer = pointer.next 
        
        remove_node_from_first = length_ll - n + 1
        if remove_node_from_first <= 0 or remove_node_from_first > length_ll:
            return head 

        pointer = head
        curr_l = 1
        while curr_l < remove_node_from_first - 1:
            curr_l += 1 
            pointer = pointer.next
        
        if remove_node_from_first == 1:
            head = head.next 
            return head 
            
        
        if pointer.next is not None:
            pointer.next = pointer.next.next
            return head
        
        

         

        


        