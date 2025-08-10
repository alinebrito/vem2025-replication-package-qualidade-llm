class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        k %= n
        if k == 0:
            return head
        slow, fast = head, head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head