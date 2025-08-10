class Solution:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        self.result = 0

        def dfs(node, high, low):
            if not node:
                return
            self.result = max(self.result, abs(node.val - high), abs(node.val - low))
            high = max(high, node.val)
            low = min(low, node.val)
            dfs(node.left, high, low)
            dfs(node.right, high, low)

        dfs(root, root.val, root.val)
        return self.result