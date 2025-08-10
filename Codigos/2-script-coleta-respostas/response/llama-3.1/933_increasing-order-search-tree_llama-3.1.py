class Solution:
    def increasingBST(self, root):
        def in_order(node):
            if not node:
                return None, float('inf')
            left, _ = in_order(node.left)
            node.left = None
            return left, node

        dummy = ListNode(0)
        curr = dummy
        root, _ = in_order(root)
        while root:
            curr.next = root
            curr = curr.next
            root = root.right
        return dummy.next