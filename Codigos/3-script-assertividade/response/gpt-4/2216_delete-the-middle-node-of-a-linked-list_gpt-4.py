class Solution:
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head):
        if not head:
            return None
        if not head.next:
            return None
        slow = fast = head
        prev = None
        count = 0
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
            count += 1
        if prev:
            prev.next = slow.next
        return head