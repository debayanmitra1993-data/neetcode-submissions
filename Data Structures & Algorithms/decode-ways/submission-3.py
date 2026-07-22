class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            if int(s) >= 1 and int(s) <= 26:
                return 1
            else:
                return 0
        
        dparr = [0]*(len(s) + 1)
        dparr[-1] = 1

        dparr[-2] = 0 if s[-1] == "0" else 1

        for idx in range(len(dparr) - 3, -1, -1):
            if s[idx] == "0":
                dparr[idx] = 0
            else:
                dparr[idx] = dparr[idx + 1]
                intval = int(s[idx : idx + 2])
                if intval >= 0 and intval <= 26:
                    dparr[idx] = dparr[idx] + dparr[idx + 2]
        return dparr[0]
        