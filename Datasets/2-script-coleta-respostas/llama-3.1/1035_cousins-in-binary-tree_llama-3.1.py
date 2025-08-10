class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(node, parent, depth, val):
            if not node:
                return
            if node.val == val:
                return (parent, depth)
            return dfs(node.left, node, depth + 1, val) or dfs(node.right, node, depth + 1, val)

        x_info = dfs(root, None, 0, x)
        y_info = dfs(root, None, 0, y)
        return x_info[1] == y_info[1] and x_info[0] != y_info[0]