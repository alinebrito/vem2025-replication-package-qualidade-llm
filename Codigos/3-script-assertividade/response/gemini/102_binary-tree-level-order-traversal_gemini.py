class Solution:
  def levelOrder(self, root):
    """
    Performs level order traversal of a binary tree.

    Args:
      root: The root node of the binary tree.

    Returns:
      A list of lists, where each inner list represents the values of nodes at a specific level.
    """
    if not root:
      return []
    result = []
    queue = [root]
    while queue:
      level_values = []
      for _ in range(len(queue)):
        node = queue.pop(0)
        level_values.append(node.val)
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)
      result.append(level_values)
    return result