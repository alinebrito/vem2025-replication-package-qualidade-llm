class Solution:
  def isValidBST(self, root):
    def isValid(node, lower_limit, upper_limit):
      if not node:
        return True
      if node.val <= lower_limit or node.val >= upper_limit:
        return False
      return isValid(node.left, lower_limit, node.val) and isValid(node.right, node.val, upper_limit)
    return isValid(root, float('-inf'), float('inf'))