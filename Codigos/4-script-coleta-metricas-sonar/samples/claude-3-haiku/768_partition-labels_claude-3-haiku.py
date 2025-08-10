class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = {c: i for i, c in enumerate(s)}
        result, max_last_seen, count = [], 0, 0
        for i, c in enumerate(s):
            max_last_seen = max(max_last_seen, last_seen[c])
            if i == max_last_seen:
                result.append(i - count + 1)
                count = i + 1
        return result