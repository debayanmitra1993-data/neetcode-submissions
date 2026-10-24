class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        currcomb = []
        allcombs = []
        self.recursiontree(n, k, currcomb, allcombs, 0, nums)
        return allcombs
    
    def recursiontree(self, n, k, currcomb, allcombs, startidx, nums):
        

        if k == 0:
            allcombs.append(currcomb.copy())
            return

        for idx in range(startidx, len(nums) - k + 1):
            ele = nums[idx]
            currcomb.append(ele)
            self.recursiontree(n, k - 1, currcomb, allcombs, idx + 1, nums)

        
            currcomb.pop()

            


        