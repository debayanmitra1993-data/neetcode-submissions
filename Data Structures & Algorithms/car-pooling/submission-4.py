import heapq 

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x : x[1])
        pq = []
        idx = 0
        curr_cap = 0
        next_drop = None
        next_pickup = None

        while True:
            if len(pq) > 0:
                next_drop = pq[0][0]
            else:
                next_drop = None
            
            next_pickup = trips[idx][1]

            if next_drop is None or next_drop > next_pickup:
                # perform pickup
                droploc = trips[idx][2]
                passcount = trips[idx][0]
                curr_cap += passcount
                if curr_cap > capacity:
                    return False
                heapq.heappush(pq, (droploc, passcount))
                idx += 1
            else:
                # perform drop
                _, passcount = heapq.heappop(pq)
                curr_cap -= passcount
            
            if idx > len(trips) - 1:
                break
        return True
                            
            

