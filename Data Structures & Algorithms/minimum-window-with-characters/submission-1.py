class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}

        required = len(need)
        formed = 0

        left = 0
        best_left = 0
        best_right = 0
        best_len = float("inf")

        for right in range(len(s)):
            char = s[right]

            if char in need:
                window[char] = window.get(char, 0) + 1

                if window[char] == need[char]:
                    formed += 1

            # Current window contains all characters required by t
            while formed == required:

                curr_len = right - left + 1

                if curr_len < best_len:
                    best_len = curr_len
                    best_left = left
                    best_right = right

                # Remove left character and shrink window
                left_char = s[left]

                if left_char in need:
                    window[left_char] -= 1

                    if window[left_char] < need[left_char]:
                        formed -= 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_left:best_right + 1]