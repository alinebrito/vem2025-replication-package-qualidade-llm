class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        
        def build_graph(node, parent):
            if not node:
                return
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            build_graph(node.left, node)
            build_graph(node.right, node)

        build_graph(root, None)
        
        queue = deque([target.val])
        seen = {target.val}
        distance = 0
        result = []

        while queue:
            if distance == k:
                result.extend(queue)
                break
            distance += 1
            for _ in range(len(queue)):
                node_val = queue.popleft()
                for neighbor in graph[node_val]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)

        return result