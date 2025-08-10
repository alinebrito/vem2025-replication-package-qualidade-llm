class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        curr = dummy = TreeNode( float("Inf") )
        stack = [dummy]
        for value in preorder:
            if value < curr.val:
                curr.left = TreeNode(value)
                curr = curr.left
            else:
                while stack and value > stack[-1].val:
                    curr = stack.pop()
                curr.right = TreeNode(value)
                curr = curr.right
            stack.append(curr)
        return dummy.left