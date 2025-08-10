class Solution:
    def reverseBetween(self, head, m, n):
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        prev = dummyNode

        for i in range(m - 1):
            prev = prev.next

        curr = prev.next
        for i in range(n - m):
            next = curr.next
            curr.next = next.next
            next.next = prev.next
            prev.next = next

        return dummyNode.next