class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '').upper()
        n = len(S)
        result = []
        for i in range(n % K, n, K):
            result.append(S[i:i+K])
        return '-'.join(result)