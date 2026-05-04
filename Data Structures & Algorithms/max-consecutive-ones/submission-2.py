class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        countones = 0
        currentlyone = False
        if nums[0] == 1:
            countones += 1
            currentlyone = True

        maxcountones = countones
        
        for idx in range(1, len(nums)):
            if nums[idx] == 1:
                currentlyone = True 
            
            if nums[idx] == 1 and currentlyone == True:
                countones += 1
                if countones > maxcountones:
                    maxcountones = countones
            else:
                countones = 0
                currentlyone = False 
            
            previous = nums[idx]
        
        return maxcountones