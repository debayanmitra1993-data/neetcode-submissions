class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "None"
        encoded_string = ""
        for mystringidx in range(len(strs)):
            mystring = strs[mystringidx]
            string_encode = ""
            for idx in range(len(mystring)):
                string_encode += str(ord(mystring[idx]))
                if idx != len(mystring) - 1:
                    string_encode += "."
            encoded_string += string_encode
            if mystringidx != len(strs) - 1:
                encoded_string += "__"
        # print("encoded_string = ", encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        output_strs = []
        s_split = s.split("__")
        for mystring in s_split:
            if mystring == "":
                output_strs.append(mystring)
                continue

            if mystring != "__":
                decoded_string = ""
                char_split = mystring.split(".")
                for char in char_split:
                    if char != ".":
                        decoded_string += chr(int(char))
                output_strs.append(decoded_string)
                # print("output_strs = ", output_strs)
        return output_strs