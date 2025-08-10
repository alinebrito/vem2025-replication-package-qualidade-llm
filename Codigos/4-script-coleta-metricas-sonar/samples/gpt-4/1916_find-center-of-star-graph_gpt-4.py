class Solution:
    def findCenter(self, edges: List[List[int]) -> int:
        node_map = {}
        for edge in edges:
            for node in edge:
                if node not in node_map:
                    node_map[node] = 1
                else:
                    node_map[node] += 1
                if node_map[node] == len(edges):
                    return node