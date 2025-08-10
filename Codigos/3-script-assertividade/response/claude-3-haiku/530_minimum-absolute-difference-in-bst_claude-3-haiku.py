class Solution:
    def getMinimumDifference(self, root):
        def fn(node, lo, hi):
            if not node:
                return float('inf')
            left = fn(node.left, lo, node.val)
            right = fn(node.right, node.val, hi)
            return min(left, right, node.val - lo, hi - node.val)
        return fn(root, float('-inf'), float('inf'))