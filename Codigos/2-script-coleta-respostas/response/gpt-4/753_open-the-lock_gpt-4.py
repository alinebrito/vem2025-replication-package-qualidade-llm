class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)
        if "0000" in dead_set:
            return -1
        queue = [("0000", 0)]
        visited = set("0000")
        
        while queue:
            current, turns = queue.pop(0)
            if current == target:
                return turns
            for i in range(4):
                for move in [-1, 1]:
                    next_wheel = (int(current[i]) + move) % 10
                    next_lock = current[:i] + str(next_wheel) + current[i+1:]
                    if next_lock not in visited and next_lock not in dead_set:
                        visited.add(next_lock)
                        queue.append((next_lock, turns + 1))
        return -1