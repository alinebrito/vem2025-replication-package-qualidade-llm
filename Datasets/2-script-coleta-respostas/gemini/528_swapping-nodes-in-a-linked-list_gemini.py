class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        first = last = head
        for i in range(k - 1):
            first = first.next
        temp = first
        while temp.next:
            last = last.next
            temp = temp.next
        first.val, last.val = last.val, first.val
        return head