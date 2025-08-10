class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
 paths = []
        if root.left:
            for path in self.binaryTreePaths(root.left):
                paths.append(str(root.val) + '->' + path)
        if root.right:
            for path in self.binaryTreePaths(root.right):
                paths.append(str(root.val) + '->' + path)
        return paths