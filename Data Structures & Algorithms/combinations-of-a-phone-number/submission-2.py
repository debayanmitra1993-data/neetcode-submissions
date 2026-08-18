class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        maps = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }

        path = []
        out = []
        self.recursiontree(0, path, maps, digits, out)
        return out
    
    def recursiontree(self, idx, path, maps, digits, out):
        if idx == len(digits):
            out.append("".join(path.copy()))

        if idx >= 0 and idx <= len(digits) - 1:
            print("idx = ", idx)
            num = digits[idx]
            for char in maps[num]:
                path.append(char)
                self.recursiontree(idx + 1, path, maps, digits, out)
        
        if len(path) > 0:
            path.pop()


        