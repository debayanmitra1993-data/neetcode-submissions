class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_str = ""
        char_idx = 0
        while char_idx < len(strs[0]):
            char = strs[0][char_idx]

            consistent = True
            for idx in range(1, len(strs)):
                string = strs[idx]
                if not char_idx <= len(string) - 1:
                    return common_str
                    
                if string[char_idx] != char:
                    consistent = False
                    return common_str
            
            if consistent == True:
                common_str += char
                char_idx += 1
            else:
                return common_str
        return common_str