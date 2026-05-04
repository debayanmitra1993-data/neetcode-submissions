class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxsofar = arr[len(arr) - 1] 
        arr[len(arr) - 1] = -1

        for idx in range(len(arr) - 2, -1, -1):
            currele = arr[idx]
            arr[idx] = maxsofar
            maxsofar = max(maxsofar, currele)
        return arr