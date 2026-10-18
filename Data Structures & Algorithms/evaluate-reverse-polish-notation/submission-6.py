class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mystack = []
        for idx in range(len(tokens)):
            ele = tokens[idx]

            if ele == "+" or ele == "-" or ele == "*" or ele == "/":
                pop1 = mystack.pop()
                pop2 = mystack.pop()
                if ele == "+":
                    newval = pop2 + pop1
                elif ele == "-":
                    newval = pop2 - pop1
                elif ele == "*":
                    newval = pop2 * pop1
                elif ele == "/":
                    newval = int(pop2 / pop1)
                mystack.append(newval)
            else:
                mystack.append(int(ele))
        return mystack[-1]