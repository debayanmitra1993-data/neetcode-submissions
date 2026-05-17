class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        leftidx = 0 
        rightidx = leftidx + 1         
        maxlen = 1
        win_set = set()
        win_set.add(s[leftidx])

        while rightidx < len(s):
            
            while s[rightidx] not in win_set:
                win_set.add(s[rightidx]) 
                rightidx += 1
                if rightidx >= len(s):
                    break
            rightidx = rightidx - 1

            maxlen = max(maxlen, rightidx - leftidx + 1)
            win_set.remove(s[leftidx])
            leftidx += 1
            rightidx += 1
            if rightidx >= len(s):
                break
        return maxlen






        