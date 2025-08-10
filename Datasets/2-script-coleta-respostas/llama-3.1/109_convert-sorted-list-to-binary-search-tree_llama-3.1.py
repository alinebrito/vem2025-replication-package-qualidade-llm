class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None

        node = TreeNode(mid.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)

        return node