class Solution:
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ''
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('None')
        return ','.join(res)

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        queue = [root]
        i = 1
        while queue and i < len(nodes):
            node = queue.pop(0)
            if nodes[i] != 'None':
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            i += 1
            if i < len(nodes) and nodes[i] != 'None':
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i += 1
        return root