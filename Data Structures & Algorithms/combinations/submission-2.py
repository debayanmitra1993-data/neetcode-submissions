class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        allcombs = []
        currcomb = []
        self.dfs(0, 0, allcombs, currcomb, n, k)
        # print("allcombs = ", allcombs)
        return allcombs
    
    def dfs(self, currnum, depth, allcombs, currcomb, n, k):
        if currnum >= 1 and currnum <= n:
            currcomb.append(currnum)
        
        if depth == k:
            allcombs.append(currcomb.copy())
            # print("allcombs = ", allcombs)
            currcomb.pop()
            # print("after pop currcomb = ", currcomb)
            return 

        for num in range(currnum + 1, n + 1):
            self.dfs(num, depth + 1, allcombs, currcomb, n, k)
        
        if len(currcomb) > 0:
            currcomb.pop()
        
        





        