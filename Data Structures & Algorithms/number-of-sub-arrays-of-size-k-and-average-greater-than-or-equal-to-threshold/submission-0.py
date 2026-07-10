class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        req_sum = k * threshold
        countsubarr = 0
        runsum = 0
        idx = 0
        while idx < k:
            runsum += arr[idx]
            idx += 1 
        
        if runsum >= req_sum:
            countsubarr += 1 

        for idx1 in range(1, len(arr) - k + 1):
            idx2 = idx1 + k - 1 
            runsum += arr[idx2] - arr[idx1 - 1]
            if runsum >= req_sum:
                countsubarr += 1 
        return countsubarr



        