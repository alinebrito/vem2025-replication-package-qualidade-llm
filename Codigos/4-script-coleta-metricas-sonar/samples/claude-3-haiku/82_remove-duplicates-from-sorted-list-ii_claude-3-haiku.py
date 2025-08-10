class Solution:
    def deleteDuplicates(self, head):
        dummy = pre = ListNode(0)
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
            else:
                pre.next = cur
                pre = pre.next
                cur = cur.next
        pre.next = None
        return dummy.next