class Solution:
    # T = O(nlogn), S = O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}

        for ele in nums:
            if ele in store:
                store[ele] += 1
            else:
                store[ele] = 1 
        
        lststore = []
        for storekey in store.keys():
            lststore.append([storekey, store[storekey]])
        
        lststore.sort(key = lambda x : x[1], reverse = True,)

        output = [None]*k
        for idx in range(k):
            output[idx] = lststore[idx][0]
        
        return output
        

        

        
        