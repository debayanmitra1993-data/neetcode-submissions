import random 

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums
    
    def quicksort(self, array, leftidx, rightidx):

        if leftidx < rightidx:
            pivot_idx = self.partition(array, leftidx, rightidx)
            self.quicksort(array, leftidx, pivot_idx - 1)
            self.quicksort(array, pivot_idx + 1, rightidx)
    
    def partition(self, array, leftidx, rightidx):
        pivot_idx = random.randint(leftidx, rightidx)
        array[leftidx], array[pivot_idx] = array[pivot_idx], array[leftidx]
        pivot_ele = array[leftidx]
        # pivot_ele = array[leftidx]

        # find the first largest value > pivot and assign previous index to that as 'i'
        i = leftidx
        while i < rightidx:
            if array[i + 1] > pivot_ele:
                break 
            else:
                i += 1 
        
        # start 'j' from (i + 1) to rest of the array..
        for j in range(i + 1, rightidx + 1):
            if array[j] <= pivot_ele:
                array[j], array[i + 1] = array[i + 1], array[j]
                i = i + 1
        
        array[leftidx], array[i] = array[i], array[leftidx]
        return i
        




        