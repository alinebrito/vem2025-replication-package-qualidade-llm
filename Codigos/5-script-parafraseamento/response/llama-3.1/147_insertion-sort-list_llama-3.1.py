class Solution:
    def insertionSortList(self, head):
        p = dummy = ListNode(0)
        while head:
            temp = head.next
            curr = dummy
            while curr.next and curr.next.val < head.val:
                curr = curr.next
            head.next = curr.next
            curr.next = head
            head = temp
        return dummy.next