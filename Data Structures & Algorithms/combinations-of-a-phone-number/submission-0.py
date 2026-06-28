class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
            
        digit_char_maps = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }

        outputlst = []
        self.dfshelper("", outputlst, digits, digit_char_maps, 0)
        return outputlst
    
    def dfshelper(self, currstr, outputlst, digits, digit_char_maps, curridx):
        if curridx > len(digits) - 1:
            outputlst.append(currstr)
            return 

        curr_digit = digits[curridx]
        curr_digit_maps = digit_char_maps[curr_digit]
        for char in curr_digit_maps:
            self.dfshelper(currstr + char, outputlst, digits, digit_char_maps, curridx + 1)


        