class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        outputs = []
        triplet_store = {}

        for idx in range(len(nums) - 2):
            curr_ele = nums[idx]
            target = -curr_ele

            # search for -curr_ele in the rest of the array...
            store = {}
            
            for jdx in range(idx + 1, len(nums)):
                ele = nums[jdx]
                if target - ele in store:
                    store[ele] = True 
                    triplet = [curr_ele, target - ele, ele]
                    triplet_str = str(curr_ele) + "_" + str(target - ele) + "_" + str(ele)
                    if triplet_str not in triplet_store:
                        outputs.append(triplet)
                        triplet_store[triplet_str] = True
                else:
                    store[ele] = True 
        
        return list(outputs)