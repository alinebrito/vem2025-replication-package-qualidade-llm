class Solution:
    def connect(self, root):
        while root and root.left:
            curr = root
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            root = root.left