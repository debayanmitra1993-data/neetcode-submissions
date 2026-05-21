class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        allcombs = []
        globaldict = {}
        self.helper(nums, target, allcombs, [], globaldict)
        print("globaldict = ", globaldict)
        print("allcombs = ", allcombs)
        return allcombs

    
    def helper(self, nums, target, allcombs, currentcomb, globaldict):
        if target == 0:
            currentcomb_dict = {}
            for ele in currentcomb:
                if ele not in currentcomb_dict:
                    currentcomb_dict[ele] = 1 
                else:
                    currentcomb_dict[ele] += 1
            currentcomb_dict_keys = list(currentcomb_dict.keys())
            currentcomb_dict_keys.sort()
            currentcomb_str = ""
            for key in currentcomb_dict_keys:
                currentcomb_str += str(key) + ":" + str(currentcomb_dict[key]) + "_"
            if currentcomb_str not in globaldict:
                globaldict[currentcomb_str] = True 
                allcombs.append(currentcomb.copy())
            return
        
        if target < 0:
            return 

        for num in nums:
            currentcomb.append(num)
            self.helper(nums, target - num, allcombs, currentcomb, globaldict)
            currentcomb.pop()        