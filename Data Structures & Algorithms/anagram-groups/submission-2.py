class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stores = {}

        for mystring in strs:
            ord_str = Solution.generate_ord_string(mystring)
            if ord_str in stores:
                stores[ord_str].append(mystring)
            else:
                stores[ord_str] = [mystring]
        print("stores = ", stores)
        output_lst = []
        for storekey in stores.keys():
            ele = stores[storekey]
            output_lst.append(ele)
        
        return output_lst
    
    @staticmethod
    def generate_ord_string(mystring):

        len_ord_string_arr = ord("z") - ord("a") + 1
        ord_string_arr = [0]*len_ord_string_arr

        for char in mystring:
            idx = ord(char) - ord("a")
            ord_string_arr[idx] += 1
        
        finalstring = ""
        for ele in ord_string_arr:
            finalstring += str(ele) + "_"
        
        return finalstring