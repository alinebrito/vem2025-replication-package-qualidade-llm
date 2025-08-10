class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(p):
            if p != parent[p]:
                parent[p] = find(parent[p])
            return parent[p]

        def union(p1, p2):
            root1, root2 = find(p1), find(p2)
            if root1 == root2:
                return False
            if rank[root1] > rank[root2]:
                parent[root2] = root1
                rank[root1] += rank[root2]
            else:
                parent[root1] = root2
                rank[root2] += rank[root1]
            return True

        components = n
        for u, v in connections:
            if union(u, v):
                components -= 1
        
        return components - 1