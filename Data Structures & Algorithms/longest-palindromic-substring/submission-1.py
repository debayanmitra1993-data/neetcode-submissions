class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen = 0
        maxsubstr = ""

        # check for odd len palindrome..
        for idx in range(len(s)):
            l, r = self.check_odd_palindrome(idx, s)
            if r - l + 1 > maxlen:
                maxlen = r - l + 1
                maxl, maxr = l, r
                maxsubstr = s[l:r+1]
            # print("ODD CASE maxl, maxr, maxsubstr = ", maxl, maxr, maxsubstr)
        
        # check for even len palindrome..
        for idx in range(len(s) - 1):
            if s[idx] == s[idx + 1]:
                l, r = self.check_even_palindrome(idx, s)
                if r - l + 1 > maxlen:
                    maxlen = r - l + 1
                    maxl, maxr = l, r
                    maxsubstr = s[l:r+1]
            # print("EVEN CASE maxl, maxr, maxsubstr = ", maxl, maxr, maxsubstr)
        
        return maxsubstr


    

    def check_odd_palindrome(self, center_idx, string):
        
        max_left_idx = center_idx
        max_right_idx = center_idx 
        maxlensofar = max_right_idx - max_left_idx + 1

        left_idx = center_idx - 1
        right_idx = center_idx + 1

        while left_idx >= 0 and right_idx <= len(string) - 1:
            if string[left_idx] == string[right_idx]:
                if right_idx - left_idx + 1 > maxlensofar:
                    maxlensofar = right_idx - left_idx + 1
                    max_left_idx = left_idx
                    max_right_idx = right_idx
                left_idx -= 1
                right_idx += 1
            else:
                break 
        
        # print("max left idx = ", max_left_idx)
        # print("max right idx = ", max_right_idx)
        # print("\n")
        return max_left_idx, max_right_idx
    
    def check_even_palindrome(self, center_idx, string):
        
        max_left_idx = center_idx
        max_right_idx = center_idx + 1
        maxlensofar = max_right_idx - max_left_idx + 1

        left_idx = center_idx - 1
        right_idx = center_idx + 2

        while left_idx >= 0 and right_idx <= len(string) - 1:
            if string[left_idx] == string[right_idx]:
                if right_idx - left_idx + 1 > maxlensofar:
                    maxlensofar = right_idx - left_idx + 1
                    max_left_idx = left_idx
                    max_right_idx = right_idx
                left_idx -= 1
                right_idx += 1
            else:
                break 
        
        # print("max left idx = ", max_left_idx)
        # print("max right idx = ", max_right_idx)
        # print("\n")
        return max_left_idx, max_right_idx

            
