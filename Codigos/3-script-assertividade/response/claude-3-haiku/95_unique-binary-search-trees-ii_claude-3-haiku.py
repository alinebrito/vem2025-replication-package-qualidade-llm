class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def node(val, left, right):
            root = TreeNode(val)
            root.left = left
            root.right = right
            return root

        def generate(start, end):
            if start > end:
                return [None]
            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate(start, i - 1)
                right_trees = generate(i + 1, end)
                for l in left_trees:
                    for r in right_trees:
                        root = node(i, l, r)
                        all_trees.append(root)
            return all_trees

        return generate(1, n) if n else []