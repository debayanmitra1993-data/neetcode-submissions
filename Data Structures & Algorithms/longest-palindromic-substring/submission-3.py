class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen = 1
        best_l_idx, best_r_idx = 0, 0

        # check for odd length palindrome
        for idx in range(1, len(s) - 1):
            lidx, ridx = self.check_odd_palindrome(idx, s)
            print("ODD lidx, ridx = ", lidx, ridx)
            if ridx - lidx + 1 > maxlen:
                maxlen = ridx - lidx + 1
                best_l_idx, best_r_idx = lidx, ridx
                print("ODD substr = ", s[best_l_idx : best_r_idx + 1])
        
        # check for even length palindrome
        for idx in range(len(s) - 1):
            if s[idx] == s[idx + 1]:
                lidx, ridx = self.check_even_palindrome(idx, idx + 1, s)
                print("EVEN lidx, ridx = ", lidx, ridx)
                if ridx - lidx + 1 > maxlen:
                    maxlen = ridx - lidx + 1
                    best_l_idx, best_r_idx = lidx, ridx
                    print("EVEN substr = ", s[best_l_idx : best_r_idx + 1])
        
        return s[best_l_idx : best_r_idx + 1]
    
    def check_even_palindrome(self, left_idx, right_idx, s):
        while True:
            if left_idx - 1 < 0 or right_idx + 1 > len(s) - 1:
                break
            else:
                if s[left_idx - 1] == s[right_idx + 1]:
                    left_idx = left_idx - 1
                    right_idx = right_idx + 1
                else:
                    break
        return left_idx, right_idx 

    def check_odd_palindrome(self, idx, s):
        left_idx = idx
        right_idx = idx

        while True:
            if left_idx - 1 < 0 or right_idx + 1 > len(s) - 1:
                break
            else:
                if s[left_idx - 1] == s[right_idx + 1]:
                    left_idx = left_idx - 1
                    right_idx = right_idx + 1
                else:
                    break
        return left_idx, right_idx