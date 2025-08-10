class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        queue = [("0000", 0)]
        visited = set(deadends)
        visited.add("0000")

        while queue:
            curr, steps = queue.pop(0)
            if curr == target:
                return steps

            for i in range(4):
                for d in [-1, 1]:
                    next_digit = str((int(curr[i]) + d) % 10)
                    next_state = curr[:i] + next_digit + curr[i+1:]
                    if next_state not in visited:
                        queue.append((next_state, steps + 1))
                        visited.add(next_state)

        return -1