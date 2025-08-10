class Solution:
    def preorderTraversal(self, root):
        ret = []
        if not root:
            return ret
        stack = [root]
        while stack:
            node = stack.pop()
            ret.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ret