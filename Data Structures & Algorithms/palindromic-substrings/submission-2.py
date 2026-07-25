class Solution:
    def countSubstrings(self, s: str) -> int:
        pal_set = set()
        
        # Check for odd length palindromes
        for idx in range(len(s)):
            self.check_palindrome(idx, idx, s, pal_set)
        
        # print("pal_set = ", pal_set)

        # check for even length palindromes
        for idx in range(len(s) - 1):
            self.check_palindrome(idx, idx + 1, s, pal_set)
        
        # print("pal_set = ", pal_set)
        return len(pal_set)
    
    def check_palindrome(self, lidx, ridx, s, pal_set):
        while True:
            if s[lidx] == s[ridx]:
                pal_set.add((lidx, ridx))
                if lidx - 1 < 0 or ridx + 1 > len(s) - 1:
                    break
                else:
                    lidx = lidx - 1
                    ridx = ridx + 1
            else:
                break 