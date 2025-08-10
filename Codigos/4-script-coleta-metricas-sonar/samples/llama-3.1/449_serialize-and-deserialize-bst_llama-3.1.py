class Solution:
    def serialize(self, root):
        if not root:
            return "[]"
        res = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return "[" + ",".join(res) + "]"

    def deserialize(self, data):
        if data == "[]":
            return None
        vals = data[1:-1].split(",")
        root = TreeNode(int(vals[0]))
        queue = [root]
        i = 1
        while queue:
            node = queue.pop(0)
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right