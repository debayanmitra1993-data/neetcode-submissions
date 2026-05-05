class Solution:
    def isValid(self, s: str) -> bool:
        bracket_maps = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stackstore = []
        for idx in range(len(s)):
            char = s[idx]

            if char in ["(", "{", "["]:
                stackstore.append(char)
            elif char in [")", "}", "]"]:
                if len(stackstore) > 0:
                    popped_ele = stackstore.pop()
                    if bracket_maps[char] == popped_ele:
                        pass
                    else:
                        return False 
                else:
                    return False
        return len(stackstore) == 0


        