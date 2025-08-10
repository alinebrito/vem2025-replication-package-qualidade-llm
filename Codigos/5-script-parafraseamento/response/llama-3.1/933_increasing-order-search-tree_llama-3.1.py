class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                self.nodes.append(node)
                inorder(node.right)

        self.nodes = []
        inorder(root)
        for i in range(len(self.nodes) - 1):
            self.nodes[i].left = None
            self.nodes[i].right = self.nodes[i + 1]
        self.nodes[-1].left = None
        self.nodes[-1].right = None
        return self.nodes[0]