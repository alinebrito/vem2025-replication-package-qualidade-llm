class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '').upper()
        size = len(S)
        first = size % K
        result = []
        if first:
            result.append(S[:first])
        for i in range(first, size, K):
            result.append(S[i:i + K])
        return '-'.join(result)