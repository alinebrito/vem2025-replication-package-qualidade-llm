class Solution:
    def removeDuplicates(self, S: str, K: int) -> str:
        SC, st, i, j = list(S), [0], 1, 1
        while i < len(SC):
            if st and SC[i] == SC[st[-1]]:
                if st[-1] + 1 == K:
                    del st[-K:]
                    i -= K - 1
                else:
                    st.append(st[-1] + 1)
            else:
                st.append(0)
            i += 1
        return ''.join(SC[j] for j in range(len(SC)) if j < st[-1])