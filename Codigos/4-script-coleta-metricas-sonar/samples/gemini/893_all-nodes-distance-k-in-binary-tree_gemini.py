class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        neighbors = defaultdict(list)
        
        def connect(parent, child):
            if parent and child:
                neighbors[parent.val].append(child.val)
                neighbors[child.val].append(parent.val)
            if child.left: connect(child, child.left)
            if child.right: connect(child, child.right)
        
        connect(None, root)
        
        queue = deque([target.val])
        visited = set([target.val])
        distance = 0
        
        while queue:
            if distance == k:
                return list(queue)
            
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in neighbors[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            distance += 1
        
        return []