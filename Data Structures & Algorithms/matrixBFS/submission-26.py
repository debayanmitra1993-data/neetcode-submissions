from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        bfsqueue = deque()
        visited = set()
        bfsqueue.append((0, 0, 0))  # (rowidx, colidx, depth)

        while len(bfsqueue) > 0:
            rowidx, colidx, depth = bfsqueue.popleft()
            if (rowidx, colidx) in visited:
                continue

            visited.add((rowidx, colidx))
            # 2 children (right, bottom)
            # right
            if colidx + 1 <= len(grid[0]) - 1:
                if grid[rowidx][colidx + 1] == 0:
                    if (rowidx, colidx + 1) not in visited:
                        bfsqueue.append((rowidx, colidx + 1, depth + 1))
        
            # bottom
            if rowidx + 1 <= len(grid) - 1:
                if grid[rowidx + 1][colidx] == 0:
                    if (rowidx + 1, colidx) not in visited:
                        bfsqueue.append((rowidx + 1, colidx, depth + 1))
        
        if rowidx == len(grid) - 1 and colidx == len(grid[0]) - 1:
            if grid[rowidx][colidx] == 0:
                return depth
        return -1