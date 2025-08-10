class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        queue = [("0000", 0)]
        visited = {"0000"}
        while queue:
            current, turns = queue.pop(0)
            if current == target:
                return turns
            for i in range(4):
                for d in [-1, 1]:
                    new_digit = (int(current[i]) + d + 10) % 10
                    neighbor = current[:i] + str(new_digit) + current[i + 1:]
                    if neighbor not in visited and neighbor not in deadends:
                        visited.add(neighbor)
                        queue.append((neighbor, turns + 1))
        return -1