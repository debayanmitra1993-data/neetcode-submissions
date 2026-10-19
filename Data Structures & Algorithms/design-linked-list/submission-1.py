class LLNode:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next 

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if not (index >= 0 and index <= self.length - 1):
            return -1
        
        i = 0
        p = self.head
        while p is not None:
            if i == index:
                return p.val
            i += 1
            p = p.next 
        return -1

    def addAtHead(self, val: int) -> None:
        if self.head is None:
            node = LLNode(val)
            self.head = node
            self.tail = node
        else:
            node = LLNode(val)
            p = self.head 
            p.prev = node
            node.next = p
            self.head = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.tail is None:
            node = LLNode(val)
            self.tail = node
            self.head = node
        else:
            node = LLNode(val)
            p = self.tail
            p.next = node
            node.prev = p
            self.tail = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index >= 0 and index <= self.length - 1:
            i = 0
            p = self.head
            while p is not None:
                if i == index - 1:
                    newnode = LLNode(val)
                    temp = p.next
                    newnode.next = temp
                    newnode.prev = p
                    p.next = newnode
                    temp.prev = newnode
                    self.length += 1
                    return 
                i += 1
                p = p.next 

    def deleteAtIndex(self, index: int) -> None:
        if not (index >= 0 and index <= self.length - 1):
            return
        
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return 
        
        if index == 0:
            p = self.head
            self.head = p.next
            self.head.prev = None
            p.next = None
        elif index == self.length - 1:
            p = self.tail
            self.tail = p.prev
            self.tail.next = None
            p.prev = None
        else:
            i = 0
            p = self.head
            while p is not None:
                if i == index - 1:
                    temp = p.next
                    p.next = temp.next
                    if temp.next is not None:
                        temp.next.prev = p
                    temp.next = None
                    temp.prev = None
                    break
                i += 1
                p = p.next 
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)