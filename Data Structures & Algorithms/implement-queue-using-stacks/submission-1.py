class MyQueue:

    def __init__(self):
        self.main_stack = []
        self.other_stack = []
        
    def push(self, x: int) -> None:
        while len(self.other_stack) > 0:
            popped_ele = self.other_stack.pop()
            self.main_stack.append(popped_ele)
        self.main_stack.append(x)

    def pop(self) -> int:
        while len(self.main_stack) > 0:
            popped_ele = self.main_stack.pop()
            self.other_stack.append(popped_ele)
        return self.other_stack.pop()

    def peek(self) -> int:
        while len(self.main_stack) > 0:
            popped_ele = self.main_stack.pop()
            self.other_stack.append(popped_ele)
        return self.other_stack[-1]

    def empty(self) -> bool:
        if len(self.main_stack) + len(self.other_stack) == 0:
            return True
        else:
            return False
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()