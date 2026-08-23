class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [x for x in range(1, n + 1)]
        output = []
        self.recursiontree(n, k, nums, 0, output, [], k)
        return output
    
    def recursiontree(self, n, k, nums, curridx, output, path, choose):
        if len(path) == choose:
            output.append(path.copy())
            return 

        for idx in range(curridx, len(nums) - k + 1):
            ele = nums[idx]
            path.append(ele)
            self.recursiontree(n, k - 1, nums, idx + 1, output, path, choose)
            if len(path) > 0:
                path.pop()







        