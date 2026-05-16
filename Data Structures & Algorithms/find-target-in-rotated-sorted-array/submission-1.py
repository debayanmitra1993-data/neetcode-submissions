class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return - 1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1 
        if len(nums) == 2:
            if nums[0] == target:
                return 0 
            if nums[1] == target:
                return 1 
            return -1

        # get the minimum index...
        print("entering get minidx function")
        min_idx = Solution.getminidx(nums)
        print("min_idx is at = ", min_idx)

        left_idx = 0
        right_idx = len(nums) - 1 

        while left_idx <= right_idx:
            mid_idx = (left_idx + right_idx) // 2
            orig_mid_idx = Solution.return_original_idx(mid_idx, min_idx, len(nums))
            
            if nums[orig_mid_idx] == target:
                return orig_mid_idx
            elif nums[orig_mid_idx] < target:
                left_idx = mid_idx + 1
            elif nums[orig_mid_idx] > target:
                right_idx = mid_idx - 1
        return -1 

    
    @staticmethod
    def return_original_idx(idx, min_idx, l):
        return (idx + min_idx) % l


    @staticmethod
    def getminidx(nums):
        if nums[0] < nums[1] and nums[0] < nums[len(nums) - 1]:
            return 0 
        
        leftidx, rightidx = 0, len(nums) - 1 

        while leftidx < rightidx:
            mididx = (leftidx + rightidx) // 2
            
            if leftidx == mididx or rightidx == mididx:
                if nums[leftidx] < nums[rightidx]:
                    return leftidx 
                else:
                    return rightidx

            if nums[mididx] < nums[mididx - 1]:
                return mididx 
            else:
                if nums[mididx] > nums[0]:
                    leftidx = mididx 
                elif nums[mididx] < nums[0]:
                    rightidx = mididx 
            



        
        