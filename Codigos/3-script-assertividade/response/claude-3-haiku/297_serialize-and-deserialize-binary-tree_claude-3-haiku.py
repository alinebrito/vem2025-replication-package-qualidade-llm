class Solution:
    def serialize(self, root):
        def doit(node):
            if not node:
                return 'None'
            else:
                return str(node.val) + ',' + self.serialize(node.left) + ',' + self.serialize(node.right)
        return doit(root)

    def deserialize(self, data):
        values = data.split(',')
        def doit():
            if values:
                val = values.pop(0)
                if val == 'None':
                    return None
                else:
                    node = TreeNode(int(val))
                    node.left = doit()
                    node.right = doit()
                    return node
        return doit()