class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) > 0:
            self.minstack.append(min(self.minstack[-1], val))
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
            self.minstack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.minstack[-1]
        
