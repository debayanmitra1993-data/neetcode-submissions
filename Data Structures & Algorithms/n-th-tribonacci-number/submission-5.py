class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        arr = [0]*(n + 1)
        arr[1] = 1
        arr[2] = 1

        for idx in range(3, len(arr)):
            arr[idx] = arr[idx - 1] + arr[idx - 2] + arr[idx - 3]
        return arr[-1]