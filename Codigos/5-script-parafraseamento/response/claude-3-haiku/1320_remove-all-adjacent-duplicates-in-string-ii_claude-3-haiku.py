class Solution:
    def removeDuplicates(self, S: str, K: int) -> str:
        SC, st, i, j = list(S), [0], 1, 1
        while i < len(SC):
            if st and SC[st[-1]] == SC[i]:
                if st[-1] + 1 == K:
                    st.pop()
                    i += 1
                else:
                    st.append(st[-1] + 1)
                    i += 1
            else:
                st.append(1)
                SC[j] = SC[i]
                i += 1
                j += 1