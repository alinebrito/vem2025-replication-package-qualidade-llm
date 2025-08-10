class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        def split(head):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow
            prev = head
            while prev.next != mid:
                prev = prev.next
            prev.next = None
            return head, mid
        
        def merge(left, right):
            dummy = ListNode(0)
            tail = dummy
            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            tail.next = left if left else right
            return dummy.next
        
        left, right = split(head)
        left = self.sortList(left)
        right = self.sortList(right)
        return merge(left, right)