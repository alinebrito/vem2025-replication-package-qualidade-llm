class Solution:
    def findDuplicateSubtrees(self, root):
        def serialize(node):
            if not node:
                return '#'
            serial = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            count[serial] += 1
            if count[serial] == 2:
                result.append(node)
            return serial
        
        from collections import defaultdict
        count = defaultdict(int)
        result = []
        serialize(root)
        return result