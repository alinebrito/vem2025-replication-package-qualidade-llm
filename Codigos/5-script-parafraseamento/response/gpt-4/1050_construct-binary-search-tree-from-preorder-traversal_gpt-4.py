class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        curr = dummy = TreeNode(float("Inf"))
        def build(preorder, bound):
            nonlocal index  
            if index == len(preorder) or preorder[index] > bound:
                return None  
            root = TreeNode(preorder[index])
            index += 1  
            root.left = build(preorder, root.val)
            root.right = build(preorder, bound)
            return root
        
        index = 0  
        return build(preorder, float("Inf"))