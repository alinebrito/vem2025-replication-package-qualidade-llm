class Solution:
    def generateTrees(self, n):
        def node(val, left, right):
            n = TreeNode(val)
            n.left = left
            n.right = right
            return n
        def trees(first, last):
            return [node(i, left, right)
                    for i in range(first, last + 1)
                    for left in trees(first, i - 1)
                    for right in trees(i + 1, last)] or [None]
        return trees(1, n)