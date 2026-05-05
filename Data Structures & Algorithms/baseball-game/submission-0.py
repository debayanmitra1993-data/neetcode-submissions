class Solution:
    def calPoints(self, operations: List[str]) -> int:
        mystack = []
        runsum = 0
        for ele in operations:
            if ele == "+":
                popped = mystack.pop()
                newele = popped + mystack[-1]
                runsum += newele
                mystack.append(popped)
                mystack.append(newele)
            elif ele == "D":
                newele = 2*mystack[-1]
                mystack.append(newele)
                runsum += newele
            elif ele == "C":
                removed_ele = mystack.pop()
                runsum -= removed_ele
            else:
                mystack.append(int(ele))
                runsum += int(ele)
            print(mystack)
        return runsum

        