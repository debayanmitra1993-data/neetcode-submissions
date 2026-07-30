class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        out_set = set()
        nums.sort()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                restsubarr = nums[j + 1:]
                duplets_lst = self.findduplets(restsubarr, target - (nums[i] + nums[j]))
                for duplet in duplets_lst:
                    if (nums[i], nums[j], duplet[0], duplet[1]) not in out_set:
                        out.append([nums[i], nums[j], duplet[0], duplet[1]])
                        out_set.add((nums[i], nums[j], duplet[0], duplet[1]))
        return out

    def findduplets(self, arr, tar):
        store = {}
        duplets = []
        duplets_set = set()
        for ele in arr:
            if (tar - ele) in store and (tar - ele, ele) not in duplets_set:
                duplets.append([tar - ele, ele])
                duplets_set.add((tar - ele, ele))
            store[ele] = True
        return duplets