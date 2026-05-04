class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1 and nums[0] == val:
            return len([])
            
        firstvalidx = 0
        lastnonvalidx = len(nums) - 1
        while firstvalidx < lastnonvalidx:
        
            while firstvalidx < len(nums):
                if nums[firstvalidx] == val:
                    break
                else:
                    firstvalidx += 1 
            
            
            while lastnonvalidx >= 0:
                if nums[lastnonvalidx] != val:
                    break
                else:
                    lastnonvalidx -= 1
            
            if firstvalidx != lastnonvalidx and firstvalidx < lastnonvalidx:
                print("performing swap between firstvalidx = ", firstvalidx, " and lastnonvalidx = ", lastnonvalidx)
                nums[firstvalidx], nums[lastnonvalidx] = nums[lastnonvalidx], nums[firstvalidx]
            else:
                break  
        return len(nums[:lastnonvalidx + 1])