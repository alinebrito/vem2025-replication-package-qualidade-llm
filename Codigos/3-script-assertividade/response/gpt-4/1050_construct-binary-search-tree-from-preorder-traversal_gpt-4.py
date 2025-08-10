class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        curr = dummy = TreeNode(float("Inf"))
        stack = []
        for value in preorder:
            node = TreeNode(value)
            if stack:
                while stack and stack[-1].val < value:
                    curr = stack.pop()
            if curr:
                curr.right = node
            else:
                dummy.left = node
            stack.append(node)
        return dummy.left