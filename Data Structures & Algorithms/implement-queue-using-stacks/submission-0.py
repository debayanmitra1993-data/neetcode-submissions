class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []
        
    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        if len(self.pop_stack) > 0:
            return self.pop_stack.pop()
        else:
            while len(self.push_stack) > 0:
                popped_ele = self.push_stack.pop()
                self.pop_stack.append(popped_ele)
            return self.pop_stack.pop()

    def peek(self) -> int:
        if len(self.pop_stack) > 0:
            return self.pop_stack[-1]
        else:
            while len(self.push_stack) > 0:
                popped_ele = self.push_stack.pop()
                self.pop_stack.append(popped_ele)
            return self.pop_stack[-1]

    def empty(self) -> bool:
        if len(self.pop_stack) + len(self.push_stack) == 0:
            return True
        else:
            return False
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()