class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '').upper()
        first_group_size = len(S) % K or K  
        reformatted = [S[:first_group_size]]
        for i in range(first_group_size, len(S), K):
            reformatted.append(S[i:i + K])
        return '-'.join(reformatted)