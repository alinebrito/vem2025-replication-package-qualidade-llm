class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count = {}
        for edge in edges:
            for node in edge:
                if node in count:
                    count[node] += 1
                else:
                    count[node] = 1
        for node, freq in count.items():
            if freq == len(edges):
                return node