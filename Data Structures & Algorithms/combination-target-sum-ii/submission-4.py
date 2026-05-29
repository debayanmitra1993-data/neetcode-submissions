class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        allcombs = [] 
        candidates.sort()
        self.helper(candidates, target, allcombs, [])
        print("allcombs = ", allcombs)
        return allcombs
        for comb in allcombs:
            comb.sort()
        print("allcombs = ", allcombs)

        finallst = []
        for comb in allcombs:
            if comb not in finallst:
                finallst.append(comb)
        return finallst
 
    def helper(self, candidates, target, allcombs, currcomb):
        if len(currcomb) > 0 and target == 0:
            allcombs.append(currcomb.copy())
            return 
            
        
        ele_store = {}
        for idx in range(len(candidates)):
            ele = candidates[idx]
            if ele > target:
                continue

            if ele in ele_store:
                continue
            else:
                ele_store[ele] = True 
            
            currcomb.append(ele)
            remaining_arr = candidates[idx + 1:]
            self.helper(remaining_arr, target - ele, allcombs, currcomb)
            currcomb.pop()