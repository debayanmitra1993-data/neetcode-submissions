class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }

        if digits == "":
            return []
        path = []
        output = []
        self.recursiondfs(path, digits, mapping, output, 0)
        return output
    
    def recursiondfs(self, path, digits, mapping, output, idx):
        if idx == len(digits):
            output.append("".join(path))
            return 
        
        digit = digits[idx]
        digit_chars = mapping[digit]
        for char in digit_chars:
            path.append(char)
            self.recursiondfs(path, digits, mapping, output, idx + 1)
            path.pop()
        





        