class Solution:
    def binaryTreePaths1(self, root):
        if not root:
            return []
        res = []
        def dfs(node, path):
            if not node.left and not node.right:
                res.append(path)
            if node.left:
                dfs(node.left, path + "->" + str(node.left.val))
            if node.right:
                dfs(node.right, path + "->" + str(node.right.val))
        dfs(root, str(root.val))
        return res