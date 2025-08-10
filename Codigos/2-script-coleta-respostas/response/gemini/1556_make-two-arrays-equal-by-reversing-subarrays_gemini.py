class Solution:
    def canBeEqual(self, targetArray: List[int], currentArray: List[int]) -> bool:
        return sorted(targetArray) == sorted(currentArray)