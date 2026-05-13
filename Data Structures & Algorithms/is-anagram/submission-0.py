class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
        
        for char in s_dict.keys():
            if char not in t_dict:
                return False 
            
            if s_dict[char] != t_dict[char]:
                return False 
        
        for char in t_dict.keys():
            if char not in s_dict:
                return False 
            
            if t_dict[char] != s_dict[char]:
                return False 
        
        return True
            
        
        