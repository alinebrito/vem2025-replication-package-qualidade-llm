class Solution:
    def deleteDuplicates(self, head):
        dummy = pre = ListNode(0)
        dummy.next = head
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        return dummy.next