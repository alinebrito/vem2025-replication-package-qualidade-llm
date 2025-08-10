class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        
        def build_graph(node, parent):
            if node:
                if parent:
                    graph[node].append(parent)
                    graph[parent].append(node)
                build_graph(node.left, node)
                build_graph(node.right, node)
        
        build_graph(root, None)
        
        queue = deque([target])
        visited = {target}
        distance = 0
        
        while queue:
            if distance == k:
                return [node.val for node in queue]
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            distance += 1
        
        return []