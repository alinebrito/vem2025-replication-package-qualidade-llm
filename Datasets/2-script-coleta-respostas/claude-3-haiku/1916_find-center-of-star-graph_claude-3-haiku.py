class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        for i in range(n):
            if edges[0][0] in edges[i] and edges[0][1] in edges[i]:
                return edges[0][0]
            elif edges[0][0] in edges[i] and edges[0][1] not in edges[i]:
                return edges[0][1]
            elif edges[0][0] not in edges[i] and edges[0][1] in edges[i]:
                return edges[0][0]