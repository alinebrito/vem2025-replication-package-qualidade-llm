class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1, v2 = list(map(int, v1.split('.'))), list(map(int, v2.split('.')))
        length = max(len(v1), len(v2))
        for i in range(length):
            rev1 = v1[i] if i < len(v1) else 0  
            rev2 = v2[i] if i < len(v2) else 0  
            if rev1 < rev2:
                return -1  
            if rev1 > rev2:
                return 1  
        return 0  