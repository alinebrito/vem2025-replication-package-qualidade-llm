class Solution:
  def isBalanced(self, root):
    def height(node):
      if not node: return 0
      leftHeight = height(node.left)
      rightHeight = height(node.right)
      if leftHeight == -1 or rightHeight == -1: return -1
      return abs(leftHeight - rightHeight) <= 1  # Check for imbalance