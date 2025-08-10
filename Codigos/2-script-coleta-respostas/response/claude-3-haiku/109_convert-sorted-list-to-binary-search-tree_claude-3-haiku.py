class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)
        
        slow, fast = head, head.next.next
        prev = None
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            prev = slow
        
        root = TreeNode(slow.val)
        right = slow.next
        prev.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(right)
        
        return root