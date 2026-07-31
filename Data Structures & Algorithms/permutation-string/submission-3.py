class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        encode_s1 = self.encode_string(s1)

        window_size = len(s1)
        for idx in range(len(s2) - window_size + 1):
            substr = s2[idx : idx + window_size]
            substr_encode = self.encode_string(substr)
            if substr_encode == encode_s1:
                print("answer is in ",substr)
                return True
        return False

    def encode_string(self, s):
        store = {}
        for char in s:
            if ord(char) not in store:
                store[ord(char)] = 1
            else:
                store[ord(char)] += 1
        store_lst = list(store.items())
        store_lst.sort(key = lambda x : x[0])

        encoder = ""
        for ele in store_lst:
            char_val = ele[0]
            char_cnt = ele[1]
            char_encode = str(char_val) + ":" + str(char_cnt) + "__"
            encoder += char_encode
        return encoder

