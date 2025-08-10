class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        result = []
        for i in range(0, n, 2 * k):
            part = s[i:i + 2 * k]
            if len(part) < k:
                result.append(part[::-1])
            elif len(part) < 2 * k:
                result.append(part[:k][::-1] + part[k:])
            else:
                result.append(part[:k][::-1] + part[k:])
        return ''.join(result)