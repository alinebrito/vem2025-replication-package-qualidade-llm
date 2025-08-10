class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        values = []
        self.inorder(root, values)
        return min(values[i] - values[i-1] for i in range(1, len(values)))

    def inorder(self, node: TreeNode, values: List[int]) -> None:
        if node:
            self.inorder(node.left, values)
            values.append(node.val)
            self.inorder(node.right, values)