class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = []
        for i in range(0, len(s), 2 * k):
            part = s[i:i + 2 * k]
            if len(part) < k:
                result.append(part[::-1])
            elif len(part) < 2 * k:
                result.append(part[:k][::-1] + part[k:])
            else:
                result.append(part[:k][::-1] + part[k:])
        return ''.join(result)