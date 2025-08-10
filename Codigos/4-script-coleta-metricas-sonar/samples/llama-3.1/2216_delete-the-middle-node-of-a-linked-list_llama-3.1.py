class Solution:
    def deleteMiddle(self, head):
        slow = head fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = slow.next
        else:
            head = None

        return head