class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        for num in arr:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        return len(counts.values()) == len(set(counts.values()))