class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        mid = self.getMiddle(head)
        midNext = mid.next

        mid.next = None

        left = self.sortList(head)
        right = self.sortList(midNext)

        sortedList = self.finalMerge(left, right)
        return sortedList

    def getMiddle(self, head):
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def finalMerge(self, a, b):
        result = None

        if not a:
            return b
        if not b:
            return a

        if a.val <= b.val:
            result = a
            result.next = self.finalMerge(a.next, b)
        else:
            result = b
            result.next = self.finalMerge(a, b.next)
        return result