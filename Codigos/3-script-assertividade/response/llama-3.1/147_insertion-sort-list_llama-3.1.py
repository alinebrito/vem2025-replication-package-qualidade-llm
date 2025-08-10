class Solution:
    def insertionSortList(self, head):
        p = dummy = ListNode(0)
        while head:
            if head.val >= dummy.val:
                head = head.next
            else:
                p1 = dummy
                while p1.next and p1.next.val < head.val:
                    p1 = p1.next
                p1.next, head.next, head = head, p1.next, head.next
                p = dummy
                while p.next:
                    p = p.next
        return dummy.next