class Solution:
    def decodeString(self, s: str) -> str:
        chk, _ = self.recursion(1, 0, s)
        print("check string = ", chk)
        return chk
    
    def recursion(self, count, idx, s):
        output_str = ""
        while s[idx] != "]":
            char = s[idx]
            s_idx = idx 
            if char.isdigit():
                while s[idx + 1].isdigit():
                    idx += 1 
                cnt = int(s[s_idx : idx + 1])
                returned_str, returned_idx = self.recursion(cnt, idx + 2, s)
                output_str = output_str + returned_str
                idx = returned_idx + 1
                if idx > len(s) - 1:
                    break 
            else:
                output_str = output_str + char
                idx += 1
                if idx > len(s) - 1:
                    break
        return count * output_str, idx
