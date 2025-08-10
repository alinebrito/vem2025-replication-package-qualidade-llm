class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverseList(head: ListNode) -> ListNode:
            prev, curr = None, head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        def to_int(head: ListNode) -> int:
            num = 0
            while head:
                num = num * 10 + head.val
                head = head.next
            return num

        def to_list(num: int) -> ListNode:
            dummy = ListNode(0)
            curr = dummy
            for digit in str(num):
                curr.next = ListNode(int(digit))
                curr = curr.next
            return dummy.next

        l1 = reverseList(l1)
        l2 = reverseList(l2)
        num = to_int(l1) + to_int(l2)
        return reverseList(to_list(num))