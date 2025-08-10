class Solution:
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("#")
        return ",".join(result)
    
    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = [root]
        i = 1
        while queue and i < len(nodes):
            node = queue.pop(0)
            if nodes[i] != "#":
                left = TreeNode(int(nodes[i]))
                node.left = left
                queue.append(left)
            i += 1
            if i < len(nodes) and nodes[i] != "#":
                right = TreeNode(int(nodes[i]))
                node.right = right
                queue.append(right)
            i += 1
        return root