class Solution:
    def postorderTraversal(self, root):
            traversal, stack = [], [(root, False)]
            while stack:
                curr, visited = stack.pop()
                if curr:
                    if visited:
                        traversal.append(curr.val)
                    else:
                        stack.append((curr, True))
                        stack.append((curr.right, False))
                        stack.append((curr.left, False))
            return traversal