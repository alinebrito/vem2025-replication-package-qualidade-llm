class Solution(object):
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head