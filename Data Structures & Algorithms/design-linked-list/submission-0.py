class LLNode:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index > self.length - 1:
            return -1
        idx = 0
        pointer = self.head
        while pointer is not None:
            if idx == index:
                return pointer.val
            else:
                pointer = pointer.next
                idx += 1

    def addAtHead(self, val: int) -> None:
        node = LLNode(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        node = LLNode(val)
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length or index < 0:
            return 
        
        node = LLNode(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            if index == 0:
                self.head.prev = node
                node.next = self.head
                self.head = node
            else:
                curridx = 0
                pointer = self.head 
                while True:
                    if curridx == index - 1:
                        break
                    else:
                        pointer = pointer.next
                        curridx += 1
                
                if pointer.next is not None:
                    temppointer = pointer.next
                    
                    temppointer.prev = node
                    node.next = temppointer 
                    
                    pointer.next = node
                    node.prev = pointer
                elif pointer.next is None:
                    pointer.next = node
                    node.prev = pointer
                    self.tail = node
        self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.length - 1:
            return 
        if self.head is None:
            return 
        
        if index == 0:
            p = self.head
            self.head = p.next
            if p.next is not None:
                p.next.prev = None
                p.next = None
            else:
                self.tail = None
        else:
            idx = 0
            pointer = self.head
            while pointer is not None:
                if idx == index - 1:
                    break
                else:
                    pointer = pointer.next
                    idx += 1
            remvp = pointer.next
            if remvp.next is None:
                pointer.next = None
                remvp.prev = None
                self.tail = pointer
            else:
                pointer.next = remvp.next
                remvp.next.prev = pointer
                remvp.prev = None
                remvp.next = None
        self.length -= 1




        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)