class LLNode:
    def __init__(self, val):
        self.val = val
        self.next = None 

class Queue:
    def __init__(self, size):
        self.head = None
        self.tail = None
        self.size = size
        self.ll_len = 0
        self.running_sum = 0
    
    def enqueue(self, val):
        if self.ll_len == 0:
            newnode = LLNode(val)
            self.head = newnode
            self.tail = newnode
            self.ll_len += 1
            self.running_sum += val
            return 
        
        newnode = LLNode(val)
        pointer = self.tail 
        pointer.next = newnode 
        self.tail = newnode 
        self.ll_len += 1
        self.running_sum += val

        if self.ll_len > self.size:
            self.dequeue()
    
    def dequeue(self):
        self.running_sum -= self.head.val
        self.ll_len -= 1
        self.head = self.head.next

class MovingAverage:

    def __init__(self, size: int):
        self.my_queue = Queue(size)

    def next(self, val: int) -> float:
        self.my_queue.enqueue(val)
        return self.my_queue.running_sum / self.my_queue.ll_len



        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
