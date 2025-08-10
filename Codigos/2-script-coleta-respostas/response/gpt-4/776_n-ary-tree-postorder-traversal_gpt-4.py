class Solution(object):
    def postorder(self, root):
        if not root:
            return []
        stack, output = [root], []
        while stack:
            node = stack.pop()
            output.append(node.val)
            stack.extend(node.children)
        return output[::-1]