class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numstore = {}
        maxele = -1
        maxsofar = 0
        for ele in nums:
            if ele not in numstore:
                numstore[ele] = 0
            numstore[ele] += 1
            if numstore[ele] > maxsofar:
                maxsofar = numstore[ele]
                maxele = ele
        return maxele

        