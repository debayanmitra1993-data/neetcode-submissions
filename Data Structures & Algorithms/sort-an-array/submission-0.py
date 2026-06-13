class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergesort(nums, 0, len(nums) - 1)
        return nums
    
    def mergesort(self, array, leftidx, rightidx):
        if leftidx < rightidx:
            mididx = (leftidx + rightidx) // 2
            self.mergesort(array, leftidx, mididx)
            self.mergesort(array, mididx + 1, rightidx)
            self.merge(array, leftidx, mididx, rightidx)
    
    def merge(self, array, leftidx, mididx, rightidx):
        leftsubarr = array[leftidx : mididx + 1]
        rightsubarr = array[mididx + 1:rightidx + 1]

        p1 = 0
        p2 = 0
        k = leftidx

        while p1 < len(leftsubarr) and p2 < len(rightsubarr):
            if leftsubarr[p1] <= rightsubarr[p2]:
                array[k] = leftsubarr[p1]
                p1 += 1
                k += 1
            else:
                array[k] = rightsubarr[p2]
                p2 += 1
                k += 1

        while p1 < len(leftsubarr):
            array[k] = leftsubarr[p1]
            p1 += 1
            k += 1
        
        while p2 < len(rightsubarr):
            array[k] = rightsubarr[p2]
            p2 += 1
            k += 1





        