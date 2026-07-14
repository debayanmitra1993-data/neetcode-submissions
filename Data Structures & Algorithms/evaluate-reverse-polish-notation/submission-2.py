class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mystack = []
        for tok in tokens:
            if tok in ["+", "-", "/", "*"]:
                pop1 = mystack.pop()
                pop2 = mystack.pop()
                if tok == "+":
                    res = pop1 + pop2
                elif tok == "-":
                    res = pop2 - pop1
                elif tok == "/":
                    res = int(pop2 / pop1)
                elif tok == "*":
                    res = pop1 * pop2
                mystack.append(res)
            else:
                mystack.append(int(tok))
        return mystack[0]