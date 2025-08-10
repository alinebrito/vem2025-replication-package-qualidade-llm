class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while i < len(name) and j < len(typed):
            if name[i] != typed[j]:
                return False
            char, count_i, count_j = name[i], 1, 1
            while i + 1 < len(name) and name[i + 1] == char:
                i += 1
                count_i += 1
            while j + 1 < len(typed) and typed[j + 1] == char:
                j += 1
                count_j += 1
            if count_i > count_j:
                return False
            i += 1
            j += 1