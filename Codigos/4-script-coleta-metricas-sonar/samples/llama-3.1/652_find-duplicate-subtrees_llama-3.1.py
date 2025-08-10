class Solution:
    def findDuplicateSubtrees(self, root):
        def serialize(node):
            if not node:
                return '#'
            return str(node.val) + ',' + serialize(node.left) + ',' + serialize(node.right)

 def traverse(node):
            if not node:
                return
            serialized = serialize(node)
            if serialized in seen:
                duplicates.add(node)
            else:
                seen.add(serialized)
            traverse(node.left)
            traverse(node.right)

        seen = set()
        duplicates = set()
        traverse(root)
        return [node.val for node in duplicates]