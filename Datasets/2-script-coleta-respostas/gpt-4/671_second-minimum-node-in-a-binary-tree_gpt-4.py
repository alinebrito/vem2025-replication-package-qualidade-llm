class Solution:
    def findSecondMinimumValue(self, root: 'TreeNode') -> int:
        def dfs(node):
            if not node:
                return
            if node.val > first[0]:
                second[0] = min(second[0], node.val)
            elif node.val == first[0]:
                dfs(node.left)
                dfs(node.right)

        first = [root.val]
        second = [float('inf')]
        dfs(root)
        return second[0] if second[0] < float('inf') else -1