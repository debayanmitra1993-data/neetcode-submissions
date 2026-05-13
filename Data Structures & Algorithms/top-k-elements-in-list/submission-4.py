class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # O(n) space
        store = {}
        for ele in nums:
            if ele in store:
                store[ele] += 1
            else:
                store[ele] = 1 
        
        freqlst = [[] for _ in range(len(nums) + 1)]

        for ele in store.keys():
            ele_count = store[ele]
            freqlst[ele_count].append(ele)
        
        output = [None]*k
        outputidx = 0
        for idx in range(len(freqlst) - 1, -1, -1): 
            
            eles = freqlst[idx]
            for ele in eles:
                output[outputidx] = ele 
                outputidx += 1
                if outputidx == k:
                    return output
        return output
            

        