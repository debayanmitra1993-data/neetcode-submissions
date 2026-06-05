class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftidx = 0
        rightidx = len(numbers) - 1

        while leftidx < rightidx:
            if numbers[leftidx] + numbers[rightidx] == target:
                return [leftidx + 1, rightidx + 1]

            if numbers[leftidx] + numbers[rightidx] < target:
                leftidx += 1
                continue
            
            if numbers[leftidx] + numbers[rightidx] > target:
                rightidx -= 1
                continue