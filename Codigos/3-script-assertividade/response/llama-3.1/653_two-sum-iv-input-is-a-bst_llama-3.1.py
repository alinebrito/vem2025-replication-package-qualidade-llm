class Solution:
    def findTarget(self, root, k):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        a = list(inorder(root))
        return any(a[i] + a[j] == k for i in range(len(a)) for j in range(i+1, len(a)))