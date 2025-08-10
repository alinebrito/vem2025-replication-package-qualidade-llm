class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1
        occurrences = list(count.values())
        return len(occurrences) == len(set(occurrences))