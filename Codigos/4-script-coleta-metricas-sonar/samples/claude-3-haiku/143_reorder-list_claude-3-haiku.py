class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Split the list into two halves
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        # Reverse the second half
        prev, curr = None, second
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Merge the two halves
        first, second = head, prev
        while second:
            next_first = first.next
            next_second = second.next
            first.next = second
            second.next = next_first
            first = next_first
            second = next_second