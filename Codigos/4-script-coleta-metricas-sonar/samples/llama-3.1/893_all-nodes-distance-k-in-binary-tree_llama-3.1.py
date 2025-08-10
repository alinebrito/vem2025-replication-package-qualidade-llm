class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def bfs(node, target, k):
            if not node:
                return []
            queue = [(node, 0)]
            visited = set()
            while queue:
                current, dist = queue.pop(0)
                if current.val == target.val:
                    return bfs_from_target(current, k)
                for neighbor in (current.left, current.right):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))
            return []

        def bfs_from_target(node, k):
            queue = [(node, 0)]
            while queue:
                current, dist = queue.pop(0)
                if dist == k:
                    return [current.val]
                for neighbor in (current.left, current.right):
                    if neighbor:
                        queue.append((neighbor, dist + 1))
            return []

        return bfs(root, target, k) + bfs_from_target(target, k)