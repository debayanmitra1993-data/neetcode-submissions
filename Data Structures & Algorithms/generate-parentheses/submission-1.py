class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        output = []
        self.recursiontree(n, 0, 0, path, output)
        return output
    
    def recursiontree(self, n, countopen, countclose, path, output):
        if countopen >= countclose and countopen <= n:
            if countopen == n and countclose == n:
                output.append("".join(path))
                return 
        

            path.append("(")
            self.recursiontree(n, countopen + 1, countclose, path, output)
            path.pop()

            path.append(")")
            self.recursiontree(n, countopen, countclose + 1, path, output)
            path.pop()

        