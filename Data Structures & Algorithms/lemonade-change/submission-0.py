class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mychange = {5 : 0, 10 : 0, 20 : 0}
        for idx in range(len(bills)):
            curr_bill = bills[idx]

            if curr_bill == 5:
                mychange[curr_bill] += 1 
            elif curr_bill == 10:
                if mychange[5] < 1:
                    return False 
                else:
                    mychange[curr_bill] += 1 
                    mychange[5] -= 1 
            elif curr_bill == 20:
                if mychange[5] >= 1:
                    mychange[5] -= 1 
                    if mychange[5] >= 2:
                        mychange[5] -= 2
                    elif mychange[10] >= 1:
                        mychange[10] -= 1
                    else:
                        return False
                    mychange[20] += 1
                else:
                    return False
        return True




        