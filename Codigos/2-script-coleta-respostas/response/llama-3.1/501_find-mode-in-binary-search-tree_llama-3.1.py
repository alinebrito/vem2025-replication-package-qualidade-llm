class Solution:
    def findMode(self, root):
        def dfs(node):
            if node:
                count[node.val] += 1
                dfs(node.left)
                dfs(node.right)

        count = {}
        dfs(root)
        max_count = max(count.values())
        return [k for k, v in count.items() if v == max_count]