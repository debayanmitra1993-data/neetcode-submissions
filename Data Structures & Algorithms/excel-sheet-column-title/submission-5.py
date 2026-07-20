class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        mappings_num_to_char = self.get_mappings()
        mappings_num_to_char[0] = "Z"
        num = columnNumber
        outputstr = ""
        while num > 0:
            remainder = num % 26  
            char = mappings_num_to_char[remainder]
            outputstr = char + outputstr 
            if remainder > 0:
                num = num // 26
            else:
                num = 0
        return outputstr

    def get_mappings(self):
        maps = {}
        for num in range(1, 26 + 1):
            maps[num] = chr(num + ord("A") - 1)
        return maps   