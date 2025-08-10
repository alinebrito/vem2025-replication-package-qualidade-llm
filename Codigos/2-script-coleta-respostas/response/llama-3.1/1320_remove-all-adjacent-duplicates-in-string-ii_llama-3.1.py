class Solution:
    def removeDuplicates(self, S: str, K: int) -> str:
        SC, st = list(S), []
        for i in range(len(SC)):
            if st and st[-1][0] == SC[i]:
                st[-1][1] += 1
                if st[-1][1] == K:
                    st.pop()
            else:
                st.append([SC[i], 1])
 return ''.join([x[0] * x[1] for x in st]).replace(K * x[0], '' for x in st)