# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k_pointers = []
        for ll in lists:
            pointer = ll
            k_pointers.append(pointer)
        
        merged_ll = None
        while self.check_break_condition(k_pointers):
            # get the minimum value from the k pointers..
            newnodeval = self.getminval(k_pointers)
            newnode = ListNode(newnodeval)
            if merged_ll is None:
                merged_pointer = newnode
                merged_ll = merged_pointer
            else:
                merged_pointer.next = newnode
                merged_pointer = newnode
        return merged_ll
    
    def getminval(self, k_pointers):
        minval = float("inf")
        minidx = -1
        for idx, pointer in enumerate(k_pointers):
            if pointer is not None:
                if pointer.val < minval:
                    minval = pointer.val
                    minidx = idx
        k_pointers[minidx] = k_pointers[minidx].next 
        return minval
    
    def check_break_condition(self, k_pointers):
        for pointer in k_pointers:
            if pointer is not None:
                return True
        return False



        