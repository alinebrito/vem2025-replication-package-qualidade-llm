class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occurrences = {}
        for num in arr:
            occurrences[num] = occurrences.get(num, 0) + 1
        return len(occurrences.values()) == len(set(occurrences.values()))