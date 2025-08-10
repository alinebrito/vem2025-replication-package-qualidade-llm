class Solution:
    def removeDuplicates(self, S: str, K: int) -> str:
        SC, st, i = list(S), [], 0
        while i < len(SC):
            st.append(SC[i])
            if len(st) >= K and all(st[-K] == st[-j] for j in range(K)):
                del st[-K:]
            i += 1
        return ''.join(st)