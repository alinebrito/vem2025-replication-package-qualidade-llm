class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        queue = deque([("0000", 0)])
        visited = set(["0000"])
        
        while queue:
            curr, steps = queue.popleft()
            if curr == target:
                return steps
            
            for i in range(4):
                for d in [-1, 1]:
                    next_num = list(curr)
                    next_num[i] = str((int(next_num[i]) + d) % 10)
                    next_num = "".join(next_num)
                    if next_num not in deadends and next_num not in visited:
                        visited.add(next_num)
                        queue.append((next_num, steps + 1))
        
        return -1