class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_path = float("-inf")

        def max_gain(node):
            nonlocal max_path
            if not node:
                return 0

            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            new_price = node.val + left_gain + right_gain
            max_path = max(max_path, new_price)

            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return max_path