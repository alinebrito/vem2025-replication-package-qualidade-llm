class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:
            first = pre.next
            second = pre.next.next
            first.next = second.next
            pre.next = second
            second.next = first
            pre = first
        return dummy.next