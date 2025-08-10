class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next