class Solution:
    def connect(self, root):
        if not root:
            return
        tail = dummy = TreeLinkNode(0)
        node = root
        while node:
            tail.next = node.left
            tail = tail.next
            if node.left:
                tail.next = node.right
                tail = tail.next
            node = node.next