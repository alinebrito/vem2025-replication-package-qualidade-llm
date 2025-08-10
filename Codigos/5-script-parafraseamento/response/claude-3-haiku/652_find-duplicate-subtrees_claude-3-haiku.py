class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def serialization(node, path):
            if node is None: return '#'
            path = f"{node.val},{serialization(node.left, path)},{serialization(node.right, path)}"
            count[path].append(node)
            return path

        count = collections.defaultdict(list)
        serialization(root, '')
        return [nodes[0] for nodes in count.values() if len(nodes) > 1]