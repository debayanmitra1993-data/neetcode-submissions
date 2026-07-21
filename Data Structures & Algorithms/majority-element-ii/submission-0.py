class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        outlst = []
        numstore = {}
        N = len(nums)
        for ele in nums:
            if ele not in numstore:
                numstore[ele] = 0
            numstore[ele] += 1
            if numstore[ele] > N//3:
                outlst.append(ele)
                numstore[ele] = float("-inf")
        return outlst
        