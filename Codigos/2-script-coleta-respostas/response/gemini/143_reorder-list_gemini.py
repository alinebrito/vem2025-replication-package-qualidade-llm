class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return head

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = self._reverseList(slow)
        head1 = head

        while head2.next:
            next1 = head1.next
            next2 = head2.next

            head1.next = head2
            head2.next = next1

            head1 = next1
            head2 = next2
        
        return head
    
    def _reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev