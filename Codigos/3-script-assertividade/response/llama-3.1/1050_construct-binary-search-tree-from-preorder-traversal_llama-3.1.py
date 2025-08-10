class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None root = TreeNode(preorder[0])
        idx = 1
        while idx < len(preorder) and preorder[idx] < root.val:
            idx += 1

        root.left = self.bstFromPreorder(preorder[1:idx])
        root.right = self.bstFromPreorder(preorder[idx:])

        return root