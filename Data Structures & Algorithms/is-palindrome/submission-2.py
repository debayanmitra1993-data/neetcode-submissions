class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ""

        for char in s:
            if char.isdigit():
                cleaned_string += str(char)
                continue 
            
            lower_char = char.lower()
            if ord(lower_char) >= ord("a") and ord(lower_char) <= ord("z"):
                cleaned_string += str(lower_char)
        print("cleaned string = ", cleaned_string)
        
        i = 0
        j = len(cleaned_string) - 1 

        while i <= j:
            if cleaned_string[i] != cleaned_string[j]:
                return False
            else:
                i += 1
                j -= 1
        return True 

