class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, par=None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root)
        
        queue = [target]
        seen = {target}
        for _ in range(k):
            new_queue = []
            for node in queue:
                for nei in (node.left, node.right, node.par):
                    if nei and nei not in seen:
                        seen.add(nei)
                        new_queue.append(nei)
            queue = new_queue
        
        return [node.val for node in queue]