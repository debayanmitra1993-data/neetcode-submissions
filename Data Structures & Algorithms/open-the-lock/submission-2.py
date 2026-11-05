from collections import deque 

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque()
        q.append(("0000", 0))
        visited = set()
        visited.add("0000")
        deadend_set = set()
        for dead in deadends:
            deadend_set.add(dead)
        if target in deadend_set:
            return -1
        if "0000" in deadend_set:
            return -1

        while len(q) > 0:
            node, depth = q.popleft()

            for idx in range(4):
                num = int(node[idx])
                if num == 0:
                    prevnum = 9
                    nextnum = 1
                elif num == 9:
                    prevnum = 8
                    nextnum = 0
                else:
                    prevnum = num - 1
                    nextnum = num + 1
                
                childnode = node[:idx] + str(prevnum) + node[idx + 1:]
                if childnode not in visited and childnode not in deadend_set:
                    if childnode == target:
                        return depth + 1
                    visited.add(childnode)
                    q.append((childnode, depth + 1))
                
                childnode = node[:idx] + str(nextnum) + node[idx + 1:]
                if childnode not in visited and childnode not in deadend_set:
                    if childnode == target:
                        return depth + 1
                    visited.add(childnode)
                    q.append((childnode, depth + 1))
        return -1






        