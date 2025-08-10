class Solution:
  def inorderTraversal(self, root):
    res = []
    stack = []
    while root or stack:
      if root:
        stack.append(root)
        root = root.left
      else:
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res