class Solution:
    def getMinimumDifference(self, root):
        def inorder(node, vals):
            if node:
                inorder(node.left, vals)
                vals.append(node.val)
                inorder(node.right, vals)

        vals = []
        inorder(root, vals)
        return min(vals[i] - vals[i-1] for i in range(1, len(vals)))