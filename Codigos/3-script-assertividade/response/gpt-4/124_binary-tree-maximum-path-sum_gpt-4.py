class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def max_gain(node):
            nonlocal max_path
            if not node:
                return 0

            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            total_path = node.val + left_gain + right_gain
            max_path = max(max_path, total_path)

            return node.val + max(left_gain, right_gain)

        max_path = float("-inf")
        max_gain(root)
        return max_path