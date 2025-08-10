class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        first = last = head
        for i in range(1, k):
            first = first.next
        node = first
        while node.next:
            last = last.next
            node = node.next
        first.val, last.val = last.val, first.val
        return head