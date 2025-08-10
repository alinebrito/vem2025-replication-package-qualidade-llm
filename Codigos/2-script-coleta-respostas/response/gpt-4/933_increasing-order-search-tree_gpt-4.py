class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                nodes.append(node)
                inorder(node.right)

        nodes = []
        inorder(root)
        for i in range(len(nodes)):
            nodes[i].left = None  
            nodes[i].right = nodes[i + 1] if i + 1 < len(nodes) else None  
        return nodes[0]