class Node:
    def __init__(self, value, nextp = None):
        self.value = value
        self.nextp = nextp      
                                           
class LinkedList:
    def __init__(self):
        self.head = None                        
        self.tail = None
        self.length = 0      
    
    def get(self, index: int) -> int:
        if index < 0 or index > self.length - 1:
            return -1
        curridx = 0 
        pointer = self.head
        while pointer is not None:
            if curridx == index:
                return pointer.value
            else:
                curridx += 1
                pointer = pointer.nextp
        
    def insertHead(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node 
        else:
            node.nextp = self.head 
            self.head = node 
        self.length += 1

    def insertTail(self, val: int) -> None:
        node = Node(val)
        if self.tail is None:
            self.tail = node 
            self.head = node 
        else:
            self.tail.nextp = node 
            self.tail = node
        self.length += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index > self.length - 1:
            return False
        if self.head is None:
            return False
        
        if index == 0:
            p = self.head 
            self.head = p.nextp
            p.nextp = None
            if self.length == 1:
                self.tail = None
        else:
            idx = 0
            pointer = self.head
            while pointer is not None:
                if idx == index - 1:
                    break
                else:
                    pointer = pointer.nextp
                    idx += 1
            removed = pointer.nextp
            pointer.nextp = removed.nextp
            removed.nextp = None
            if index == self.length - 1:
                self.tail = pointer
        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        out = [-1]*self.length
        print("out = ", out)
        pointer = self.head 
        for idx in range(self.length):
            out[idx] = pointer.value
            pointer = pointer.nextp
            print("iterate out = ", out)
        return out