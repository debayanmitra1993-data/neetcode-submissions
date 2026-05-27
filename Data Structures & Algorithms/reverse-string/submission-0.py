class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        idx =0 
        jdx = len(s) - 1 

        while idx < jdx:
            s[idx], s[jdx] = s[jdx], s[idx]
            idx += 1
            jdx -= 1
        return s

        