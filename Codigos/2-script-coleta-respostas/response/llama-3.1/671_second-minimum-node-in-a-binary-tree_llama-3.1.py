class Solution(object):
    def findSecondMinimumValue(self, root):
        if not root: return -1
        ar = set()
        def dfs(root):
            ar.add(root.val)
            if root.left:
                if root.left.val != root.val:
                    dfs(root.left)
            if root.right:
                if root.right.val != root.val:
                    dfs(root.right)
        dfs(root)
        ar.remove(min(ar))
        return min(ar) if ar else -1