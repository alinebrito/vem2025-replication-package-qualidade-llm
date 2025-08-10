class Solution:
    def isLongPressedName(self, name, typed):
        i = 0
        j = 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        while j > 0 and j < len(typed) and typed[j] == typed[j - 1]:
            j += 1
        return i == len(name) and j == len(typed)