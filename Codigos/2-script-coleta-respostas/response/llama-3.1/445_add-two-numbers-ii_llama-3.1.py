class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0
            sum = carry + x1 + x2
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next