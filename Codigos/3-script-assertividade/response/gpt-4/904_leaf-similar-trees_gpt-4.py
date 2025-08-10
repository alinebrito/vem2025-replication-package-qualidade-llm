class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def getLeaves(root):
            leaves = []
            if root:
                if not root.left and not root.right:
                    leaves.append(root.val)
                leaves.extend(getLeaves(root.left))
                leaves.extend(getLeaves(root.right))
            return leaves
        
        return getLeaves(root1) == getLeaves(root2)