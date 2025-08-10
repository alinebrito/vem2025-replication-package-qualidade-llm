class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parent_depth = {}
        def dfs(node, parent, depth):
            if not node:
                return
            if node.val == x:
                parent_depth[x] = (parent, depth)
            elif node.val == y:
                parent_depth[y] = (parent, depth)
            else:
                dfs(node.left, node, depth + 1)
                dfs(node.right, node, depth + 1)
        dfs(root, None, 0)
        p1, d1 = parent_depth.get(x, (None, None))
        p2, d2 = parent_depth.get(y, (None, None))
        return p1 != p2 and d1 == d2