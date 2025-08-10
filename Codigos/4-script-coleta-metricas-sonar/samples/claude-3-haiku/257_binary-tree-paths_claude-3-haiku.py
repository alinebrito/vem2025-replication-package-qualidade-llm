class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        paths = []
        self.dfs(root, "", paths)
        return paths

    def dfs(self, node, path, paths):
        path += str(node.val)
        if not node.left and not node.right:
            paths.append(path)
            return
        if node.left:
            self.dfs(node.left, path + "->", paths)
        if node.right:
            self.dfs(node.right, path + "->", paths)