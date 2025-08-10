class Solution:
    def reverseBetween(self, head, left, right):
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            temp = cur.next            cur.next = temp.next
            temp.next = pre.next
 pre.next = temp

        return dummy.next