class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def serialization(node, path):
            if node is None: return '#'
            path = f"{node.val} {serialization(node.left, path)} {serialization(node.right, path)}"
            if path in seen:
                if path not in count:
                    ans.append(node)
                count[path] += 1
            else:
                seen.add(path)
                count[path] = 1
            return path

        seen, count, ans = set(), {}, []
        serialization(root, '')
        return ans