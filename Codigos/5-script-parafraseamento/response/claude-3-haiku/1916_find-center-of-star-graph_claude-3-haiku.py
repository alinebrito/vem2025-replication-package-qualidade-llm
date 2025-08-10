class Solution:

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        for i in range(1, n+1):
            if i in edges[0] and i in edges[1]: