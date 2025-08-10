class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = list(map(int, version1.split('.'))), list(map(int, version2.split('.')))
        
        for i in range(max(len(v1), len(v2))):
            v1_part = v1[i] if i < len(v1) else 0
            v2_part = v2[i] if i < len(v2) else 0
            
            if v1_part < v2_part:
                return -1
            elif v1_part > v2_part:
                return 1
        
        return 0