class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        for startidx in range(len(gas)):
            cargasamt = 0
            isvalidstartidx = True
            for idx in range(len(gas)):
                curr_idx = (startidx + idx) % len(gas)
                cargasamt = cargasamt + gas[curr_idx]
                if cargasamt >= cost[curr_idx]:
                    cargasamt = cargasamt - cost[curr_idx]
                else:
                    isvalidstartidx = False
                    break
            if isvalidstartidx == True:
                return startidx
