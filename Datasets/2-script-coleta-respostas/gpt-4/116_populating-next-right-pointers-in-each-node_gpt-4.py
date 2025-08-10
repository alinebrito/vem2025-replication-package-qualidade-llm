class Solution:
    def connect(self, root):
        while root and root.left:
            leftmost = root
            while leftmost:
                leftmost.left.next = leftmost.right
                if leftmost.next:
                    leftmost.right.next = leftmost.next.left
                leftmost = leftmost.next
            root = root.left