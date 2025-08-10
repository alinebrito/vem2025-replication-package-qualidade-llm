class Solution(object):
    def postorder(self, root):
        if not root:
            return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children)
        return res[::-1]