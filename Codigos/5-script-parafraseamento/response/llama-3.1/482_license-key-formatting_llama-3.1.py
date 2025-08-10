class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '').lower()
        n = len(S)
        first_group_size = n % K or K
        result = [S[:first_group_size]]
        for i in range(first_group_size, n, K):
            result.append(S[i:i + K])
        return '-'.join(result)