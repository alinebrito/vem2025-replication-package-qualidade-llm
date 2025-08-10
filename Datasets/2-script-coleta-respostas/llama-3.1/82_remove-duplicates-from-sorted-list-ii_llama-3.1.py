class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next == cur:
                pre = pre.next
            else:
                pre.next = cur.next
            cur = cur.next
        return dummy.next