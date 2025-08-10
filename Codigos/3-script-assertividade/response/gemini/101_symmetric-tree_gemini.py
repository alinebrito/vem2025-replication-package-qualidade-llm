class Solution:
  def isSymmetric(self, root):
    """
    Checks if a binary tree is a mirror of itself (symmetric).

    Args:
      root: The root node of the binary tree.

    Returns:
      True if the tree is symmetric, False otherwise.
    """

    def isMirror(self, left, right):
      if not left and not right:
        return True
      if not left or not right:
        return False
      return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

    return isMirror(root, root)
