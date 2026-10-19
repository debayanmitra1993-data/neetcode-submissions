class LLNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def get(self, index: int) -> int:
        i = 0
        p = self.head
        while p is not None:
            if i == index:
                return p.val
            i += 1
            p = p.next
        return -1
        
    def insertHead(self, val: int) -> None:
        if self.head is None:
            self.head = LLNode(val)
            self.tail = self.head 
        else:
            newnode = LLNode(val)
            newnode.next = self.head
            self.head = newnode
        self.length += 1

    def insertTail(self, val: int) -> None:
        if self.tail is None:
            self.tail = LLNode(val)
            self.head = self.tail
        else:
            newnode = LLNode(val)
            self.tail.next = newnode
            self.tail = newnode
        self.length += 1

    def remove(self, index: int) -> bool:
        if not (index >= 0 and index <= self.length - 1):
            return False
        
        if index == 0:
            p = self.head
            self.head = p.next
            p.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
        else:
            i = 0
            p = self.head
            while p is not None:
                if i == index - 1:
                    temp = p.next
                    p.next = temp.next
                    temp.next = None
                    if p.next is None:
                        self.tail = p
                i += 1
                p = p.next
            self.length -= 1
        return True

    def getValues(self) -> List[int]:
        p = self.head
        out = []
        while p is not None:
            out.append(p.val)
            p = p.next 
        return out