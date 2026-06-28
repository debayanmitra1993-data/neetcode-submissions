class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]

        currstr = "("
        outlst = []
        self.dfshelper(n, currstr,1 , 0, outlst)
        return outlst
    
    def dfshelper(self, n, currstr, countopen, countclose, outlst):
        # check if node is valid, else return
        if countopen > n or countclose > n or countclose > countopen:
            return 
        
        # check if we reached terminal node
        if countopen == n and countclose == n and countopen == countclose:
            outlst.append(currstr)
            # print("outlst = ", outlst)
            return 
        
        self.dfshelper(n, currstr + "(", countopen + 1, countclose, outlst)
        self.dfshelper(n, currstr + ")", countopen, countclose + 1, outlst)


