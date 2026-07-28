class Solution:
    def validPalindrome(self, s: str) -> bool:
        if self.checkpalindrome(s):
            return True
        
        for idx in range(len(s)):
            mystr = s[:idx] + s[idx + 1:]
            if self.checkpalindrome(mystr):
                return True
        return False

    
    def checkpalindrome(self, s):
        i, j = 0, len(s) - 1
        while i<=j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True