class Solution:
    def serialize(self, root):
        def doit(node):
            if not node:
                return ['#']
            return [str(node.val)] + doit(node.left) + doit(node.right)
        return ','.join(doit(root))

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None  
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node  
        vals = iter(data.split(','))
        return doit()