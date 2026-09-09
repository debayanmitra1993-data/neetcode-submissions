class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        gcdval = self.findgcd(len(str1), len(str2))
        return str1[:gcdval]
    
    def findgcd(self, num1, num2):
        num1_factors_lst = []
        self.findfactors(num1, num1_factors_lst)
        num1_factors_store = {}
        for fact in num1_factors_lst:
            if fact not in num1_factors_store:
                num1_factors_store[fact] = 0
            num1_factors_store[fact] += 1

        num2_factors_lst = []
        self.findfactors(num2, num2_factors_lst)
        num2_factors_store = {}
        for fact in num2_factors_lst:
            if fact not in num2_factors_store:
                num2_factors_store[fact] = 0
            num2_factors_store[fact] += 1
        
        gcdvalue = 1
        for fact in num1_factors_store.keys():
            if fact in num2_factors_store:
                gcdvalue = gcdvalue * (fact ** min(num2_factors_store[fact], num1_factors_store[fact]))
        return gcdvalue
        

    
    def findfactors(self, num, factors_lst):
        if num == 1:
            return 
        
        for factor in range(2, num + 1):
            if num % factor == 0:
                factors_lst.append(factor)
                self.findfactors(num // factor, factors_lst)
                break