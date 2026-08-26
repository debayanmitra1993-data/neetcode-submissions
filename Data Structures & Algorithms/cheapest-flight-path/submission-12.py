from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        shortest_paths = {}
        for node in range(n):
            graph[node] = []
            shortest_paths[node] = float("inf")
        for flight in flights:
            flight_src, flight_dest, cost = flight[0], flight[1], flight[2]
            graph[flight_src].append((flight_dest, cost))

        shortest_paths[src] = 0

        for hop in range(k + 1):
            temp_shortest_paths = shortest_paths.copy()
            for flight in flights:
                src_city, dest_city, cost = flight[0], flight[1], flight[2]
                if cost + shortest_paths[src_city] < temp_shortest_paths[dest_city]:
                    temp_shortest_paths[dest_city] = cost + shortest_paths[src_city]
            shortest_paths = temp_shortest_paths.copy()
        
        if shortest_paths[dst] == float("inf"):
            return -1
        return shortest_paths[dst]

                    

                
        
        