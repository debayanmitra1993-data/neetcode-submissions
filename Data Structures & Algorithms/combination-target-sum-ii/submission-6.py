class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        store = {}
        path = []
        self.recursiontree(candidates, target, store, path, 0)
        return [list(k) for k,v in store.items()]
    
    def recursiontree(self, candidates, target, store, path, curridx):
        if target == 0:
            if len(path) > 0:
                if tuple(path) not in store:
                    store[tuple(path)] = True
            return
        
        
        for idx in range(curridx, len(candidates)):
            if idx > curridx and candidates[idx] == candidates[idx - 1]:
                continue
            ele = candidates[idx]
            if target - ele >= 0:
                path.append(ele)
                self.recursiontree(candidates, target - ele, store, path, idx + 1)
                path.pop()
            else:
                break