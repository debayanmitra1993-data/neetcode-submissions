class LLNode:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next 

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self) -> bool:
        return self.length == 0

    def append(self, value: int) -> None:
        newnode = LLNode(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            p = self.tail
            p.next = newnode
            newnode.prev = p
            self.tail = newnode
        self.length += 1

    def appendleft(self, value: int) -> None:
        newnode = LLNode(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            p = self.head
            p.prev = newnode
            newnode.next = p
            self.head = newnode
        self.length += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        if self.length == 1:
            val = self.tail.val
            self.head = None
            self.tail = None
            self.length -= 1
            return val 
        else:
            p = self.tail
            val = p.val
            self.tail = p.prev
            self.tail.next = None
            p.prev = None
            self.length -= 1
            return val


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        if self.length == 1:
            val = self.tail.val
            self.head = None
            self.tail = None
            self.length -= 1
            return val 
        else:
            p = self.head
            val = p.val
            self.head = p.next
            self.head.prev = None
            p.next = None
            self.length -= 1
            return val

        
