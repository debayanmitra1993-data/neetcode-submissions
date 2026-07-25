class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = len(s)
        for substrlen in range(2, len(s) + 1):
            for idx in range(len(s) - substrlen + 1):
                substr = s[idx : idx + substrlen]
                boolchk = self.check_palindrome(substr)
                if boolchk == True:
                    cnt += 1
        return cnt
    
    def check_palindrome(self, substr):
        lidx = 0
        ridx = len(substr) - 1 

        while lidx <= ridx:
            if substr[lidx] != substr[ridx]:
                return False
            lidx = lidx + 1
            ridx = ridx - 1
        return True