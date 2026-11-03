import heapq 

class Solution:
    def reorganizeString(self, s: str) -> str:
        pq = []
        outs = ""
        mystack = []

        store = {}
        for char in s:
            if char not in store:
                store[char] = 0
            store[char] += 1
        
        for char in store.keys():
            cnt = store[char]
            heapq.heappush(pq, (-cnt, char))
        
        while len(outs) < len(s):
            if len(pq) == 0:
                return ""

            cnt, char = heapq.heappop(pq)
            outs += char
            cnt += 1
            
            if len(mystack) > 0:
                cntprev, charprev = mystack.pop()
                heapq.heappush(pq, (cntprev, charprev))

            if cnt < 0:
                mystack.append((cnt, char))
        
        return outs