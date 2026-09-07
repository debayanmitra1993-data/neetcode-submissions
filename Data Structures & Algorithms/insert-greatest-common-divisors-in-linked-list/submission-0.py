# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head 
        while pointer.next is not None:
            newnode = ListNode(val = self.findgcd(pointer.val, pointer.next.val))
            newnode.next = pointer.next
            pointer.next = newnode 

            pointer = pointer.next.next 
        return head 
    
    def findgcd(self, num1, num2):
        num1factors = self.findfactors(num1)
        num2factors = self.findfactors(num2)

        gcdval = 1
        for factor in num1factors.keys():
            if factor in num2factors:
                gcdval *= factor ** min(num1factors[factor], num2factors[factor])
        return gcdval

    def findfactors(self, num):
        factorlst = []
        self.recursionfactors(num, factorlst)
        factorstore = {}
        for factor in factorlst:
            if factor not in factorstore:
                factorstore[factor] = 0
            factorstore[factor] += 1
        return factorstore
    
    def recursionfactors(self, num, factorlst):
        if num == 1:
            return 
        
        foundfactor = False
        for factor in range(2, num + 1):
            if num % factor == 0:
                factorlst.append(factor)
                foundfactor = True
                break
        
        if foundfactor == True:
            self.recursionfactors(num // factor, factorlst)