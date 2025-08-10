class Solution:
    def connect(self, root):
        while root and root.left:
            level = root
            while level:
                level.left.next = level.right
                if level.next:
                    level.right.next = level.next.left
                level = level.next
            root = root.left