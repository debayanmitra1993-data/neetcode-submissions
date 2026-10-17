class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        runsum = 0
        countsubarr = 0
        minsum = threshold * k

        for idx in range(k):
            runsum += arr[idx]
        if runsum >= minsum:
            countsubarr += 1
        
        for idx in range(1, len(arr) -k + 1):
            addele = arr[idx + k - 1]
            subtractele = arr[idx - 1]

            runsum = runsum + addele - subtractele
            if runsum >= minsum:
                countsubarr += 1
        
        return countsubarr