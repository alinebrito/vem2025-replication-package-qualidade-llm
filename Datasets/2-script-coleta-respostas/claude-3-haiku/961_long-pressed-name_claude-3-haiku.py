class Solution:
    def isLongPressedName(self, name, typed):
        i, j = 0, 0
        while i < len(name) and j < len(typed):
            if name[i] != typed[j]:
                if i > 0 and name[i] == name[i-1] and typed[j] == typed[j-1]:
                    j += 1
                else:
                    return False
            else:
                i += 1
                j += 1
        return i == len(name)