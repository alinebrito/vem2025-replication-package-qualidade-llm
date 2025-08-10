class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        while head:
            curr = head
            head = head.next
            p = dummy
            while p.next and p.next.val < curr.val:
                p = p.next
            curr.next = p.next
            p.next = curr
        return dummy.next