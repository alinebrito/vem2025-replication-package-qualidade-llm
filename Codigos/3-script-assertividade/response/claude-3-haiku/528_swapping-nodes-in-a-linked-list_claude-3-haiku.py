class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        first = last = head
        for _ in range(k-1):
            first = first.next
        curr = first
        while curr.next:
            curr = curr.next
            last = last.next
        first.val, last.val = last.val, first.val
        return head