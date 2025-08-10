class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1, v2 = list(map(int, v1.split('.'))), list(map(int, v2.split('.')))
 max_len = max(len(v1), len(v2))
        v1, v2 = v1 + [0] * (max_len - len(v1)), v2 + [0] * (max_len - len(v2))
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1 else:
            return 0