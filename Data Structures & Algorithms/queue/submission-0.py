class LLNode:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class Deque:
    def __init__(self):
        self.rear = None
        self.front = None
        self.length = 0

    def isEmpty(self) -> bool:
        if self.length > 0:
            return False
        else:
            return True

    def append(self, value: int) -> None:
        node = LLNode(value)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            node.prev = self.rear
            self.rear.next = node
            self.rear = node
        self.length += 1

    def appendleft(self, value: int) -> None:
        node = LLNode(value)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node
        self.length += 1

    def pop(self) -> int:
        if self.length == 0:
            return -1
        if self.length == 1:
            catch = self.front.value
            self.front = None
            self.rear = None
            self.length -= 1
            return catch

        
        pointer = self.rear
        self.rear = pointer.prev
        self.rear.next = None
        pointer.prev = None
        self.length -= 1
        return pointer.value

    def popleft(self) -> int:
        if self.length == 0:
            return -1
        if self.length == 1:
            catch = self.front.value
            self.front = None
            self.rear = None
            self.length -= 1
            return catch
            
        pointer = self.front
        self.front = pointer.next
        self.front.prev = None
        pointer.next = None
        self.length -= 1
        return pointer.value
        
