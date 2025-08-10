class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        curr = dummy = TreeNode(float("Inf"))
        stack = []
        root = None
        for val in preorder:
            node = TreeNode(val)
            if val < curr.val:
                curr.left = node
                stack.append(curr)
                curr = node
            else:
                while stack and val > stack[-1].val:
                    curr = stack.pop()
                curr.right = node
                curr = node
            root = curr
        return root