from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)        

    def pop(self) -> int:
        L = len(self.queue)
        for idx in range(L):
            popped_ele = self.queue.popleft()
            if idx == L - 1:
                return popped_ele
            else:
                self.push(popped_ele)

    def top(self) -> int:
        L = len(self.queue)
        for idx in range(L):
            popped_ele = self.queue.popleft()
            if idx == L - 1:
                self.push(popped_ele)
                return popped_ele
            else:
                self.push(popped_ele)


    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False
        
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()