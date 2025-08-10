class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(node, parent, depth):
            if not node:
                return  
            if node.val == x:
                self.x_info = (parent, depth)
            elif node.val == y:
                self.y_info = (parent, depth)
            dfs(node.left, node.val, depth + 1)
            dfs(node.right, node.val, depth + 1)

        self.x_info = self.y_info = (None, -1)
        dfs(root, None, 0)
        return self.x_info[1] == self.y_info[1] and self.x_info[0] != self.y_info[0]