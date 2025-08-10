class Solution:
    def insertionSortList(self, head):
        p = dummy = ListNode(0)
        curr = head
        while curr:
            tmp = curr.next
            p = dummy
            while p.next and p.next.val < curr.val:
                p = p.next
            curr.next = p.next
            p.next = curr
            curr = tmp
        return dummy.next