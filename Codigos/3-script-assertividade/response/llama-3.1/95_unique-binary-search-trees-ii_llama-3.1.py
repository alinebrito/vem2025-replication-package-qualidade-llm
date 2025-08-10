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
                for l in left_trees:
                    for r in right_trees:
                        all_trees.append(node(i, l, r))
            return all_trees
        
        return generate(1, n) if n else []