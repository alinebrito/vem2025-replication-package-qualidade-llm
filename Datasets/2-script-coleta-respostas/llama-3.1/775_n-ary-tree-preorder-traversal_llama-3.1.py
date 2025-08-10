class Solution:
    def preorder(self, root):
        if not root:
            return []
        stack, output = [root], []
        while stack:
            node = stack.pop()
            output.append(node.val)
            stack.extend(reversed(node.children))
        return output