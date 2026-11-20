class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        path = []
        self.recursiontree(n, k, 1, path, output)
        return output
    
    def recursiontree(self, n, k, idx, path, output):
        if k == 0:
            output.append(path.copy())
            return

        for i in range(idx, n - k + 2):
            path.append(i)
            self.recursiontree(n, k - 1, i + 1, path, output)
            path.pop()