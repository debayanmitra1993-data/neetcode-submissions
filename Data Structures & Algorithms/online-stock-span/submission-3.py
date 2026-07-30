class StockSpanner:

    def __init__(self):
        # (price, span) elements in this stack
        self.stack = []

    def next(self, price: int) -> int:
        if len(self.stack) == 0:
            self.stack.append((price, 1))
            return 1
        
        if price == self.stack[-1][0]:
            self.stack.append((price, 1 + self.stack[-1][1]))
        elif price < self.stack[-1][0]:
            self.stack.append((price, 1))
        elif price > self.stack[-1][0]:
            totspan = 1
            idx = len(self.stack) - 1
            while idx >= 0:
                if price > self.stack[idx][0]:
                    currspan = self.stack[idx][1] 
                    totspan += currspan
                    idx = idx - currspan
                else:
                    break
            self.stack.append((price, totspan))
        return self.stack[-1][1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)