class Solution:
    def serialize(self, root: TreeNode) -> str:
        def build_string(node):
            if not node:
                return 'X'
            return str(node.val) + ',' + build_string(node.left) + ',' + build_string(node.right)
        
        return build_string(root)

    def deserialize(self, data: str) -> TreeNode:
        def build_tree(nodes):
            val = next(nodes)
            if val == 'X':
                return None
            node = TreeNode(int(val))
            node.left = build_tree(nodes)
            node.right = build_tree(nodes)
            return node
        
        nodes = iter(data.split(','))
        return build_tree(nodes)