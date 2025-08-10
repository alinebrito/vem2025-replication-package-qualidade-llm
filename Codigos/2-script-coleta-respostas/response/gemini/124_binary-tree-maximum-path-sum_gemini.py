class Solution:
  def maxPathSum(self, root):
    max_path = float("-inf")
    def dfs(node):
      if not node: return 0
      left_sum = max(0, dfs(node.left))
      right_sum = max(0, dfs(node.right))
      current_sum = node.val + left_sum + right_sum
      nonlocal max_path
      max_path = max(max_path, current_sum)
      return node.val + max(left_sum, right_sum)
    dfs(root)
    return max_path