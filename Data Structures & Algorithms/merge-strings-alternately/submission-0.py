class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx1, idx2 = 0, 0
        newstr = ""
        while idx1 < len(word1) and idx2 < len(word2):
            newstr += word1[idx1]
            idx1 += 1

            newstr += word2[idx2]
            idx2 += 1
        while idx1 < len(word1):
            newstr += word1[idx1]
            idx1 += 1
        while idx2 < len(word2):
            newstr += word2[idx2]
            idx2 += 1
        return newstr