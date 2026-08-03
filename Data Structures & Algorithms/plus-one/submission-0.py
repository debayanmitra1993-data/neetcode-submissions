import math
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        out = digits.copy()
        carryover = 0

        for idx in range(len(digits) - 1, -1, -1):
            if idx == len(digits) - 1:
                if digits[idx] + 1 < 10:
                    out[idx] = out[idx] + 1
                    return out 
                else:
                    out[idx] = 0
                    carryover = 1
            else:
                if out[idx] + carryover < 10:
                    out[idx] = out[idx] + carryover
                    return out
                else:
                    out[idx] = 0
                    carryover = 1
        if carryover > 0:
            return [carryover] + out
        else:
            return out




