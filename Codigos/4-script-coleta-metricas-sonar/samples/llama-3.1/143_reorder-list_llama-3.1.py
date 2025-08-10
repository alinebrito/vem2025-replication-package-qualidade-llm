class Solution:
    def _splitList(self, head):
        slow = head
        fast = head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        return slow, head