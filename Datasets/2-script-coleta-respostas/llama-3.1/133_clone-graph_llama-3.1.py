class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        visited = {}
        def clone(node):
            if node in visited:
                return visited[node]
            copy = Node(node.val, [])
            visited[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(clone(n))
            return copy

        return clone(node)