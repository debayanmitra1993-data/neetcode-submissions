class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dparr = [False]*(len(s) + 1)
        dparr[len(dparr) - 1] = True

        for idx in range(len(dparr) - 2, -1, -1):
            char = s[idx]
            for word in wordDict:
                len_word = len(word)
                if s[idx : idx + len_word] == word:
                    dparr[idx] = dparr[idx + len_word]
                    if dparr[idx] == True:
                        break 
        print("dparr = ", dparr)
        return dparr[0]
        
            


        