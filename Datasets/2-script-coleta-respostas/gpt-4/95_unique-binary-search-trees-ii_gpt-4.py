class Solution:
    def generateTrees(self, n):
        def node(val, left, right):
            return [val, left, right]

        def generate(start, end):
            if start > end:
                return [None]
            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate(start, i - 1)
                right_trees = generate(i + 1, end)
                for left in left_trees:
                    for right in right_trees:
                        all_trees.append(node(i, left, right))
            return all_trees

        if n == 0:
            return []
        return generate(1, n)