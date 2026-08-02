class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        shortest_paths = {}
        for edge in flights:
            mysrc, mydest, mywt = edge[0], edge[1], edge[2]
            if mysrc not in shortest_paths:
                shortest_paths[mysrc] = float("inf")
            if mydest not in shortest_paths:
                shortest_paths[mydest] = float("inf")
        shortest_paths[src] = 0
        

        for hop in range(k + 1):
            temp_shortest_paths = shortest_paths.copy()
            for edge in flights:
                mysrc, mydest, mywt = edge[0], edge[1], edge[2]
                if shortest_paths[mysrc] + mywt < temp_shortest_paths[mydest]:
                    temp_shortest_paths[mydest] = shortest_paths[mysrc] + mywt
            shortest_paths = temp_shortest_paths.copy()
        
        print("shortest_paths", shortest_paths)
        if shortest_paths[dst] == float("inf"):
            return -1
        else:
            return shortest_paths[dst]


        