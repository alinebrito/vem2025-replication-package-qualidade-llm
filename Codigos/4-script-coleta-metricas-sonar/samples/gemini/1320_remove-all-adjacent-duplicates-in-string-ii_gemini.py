class Solution:
    def removeDuplicates(self, S: str, K: int) -> str:
        SC, st, i, j = list(S), [0], 1, 1
        while j < len(S):
            SC[i] = S[j]
            if SC[i] != SC[i - 1]:
                i += 1
                j += 1
            elif j - st[-1] + 1 == K:
                i = st[-1]
                st.pop()
                j += 1
            else:
                i += 1
                j += 1
            if i > st[-1]:
                st.append(i)
        return "".join(SC[:i])