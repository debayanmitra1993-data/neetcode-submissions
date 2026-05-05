# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2

        if list2 is None:
            return list1
        
        # assign mainlist and insertlist
        if list1.val <= list2.val:
            head = list1 
            self.mergehelper(list1, list2)
        else:
            head = list2
            self.mergehelper(list2, list1)
        
        return head 
    
    def mergehelper(self, mainpointer, insertpointer):
        while True:
            if mainpointer.val <= insertpointer.val:
                if mainpointer.next is not None:
                    if insertpointer.val <= mainpointer.next.val:
                        # insert in between...
                        tempinsert = insertpointer
                        insertpointer = insertpointer.next
                        tempinsert.next = mainpointer.next
                        mainpointer.next = tempinsert

                        mainpointer = tempinsert

                        # finished inserting all elements...so break out...
                        if insertpointer is None:
                            break
                    else:
                        mainpointer = mainpointer.next 
                elif mainpointer.next is None:
                    mainpointer.next = insertpointer
                    break 
            else:
                pass
                 


