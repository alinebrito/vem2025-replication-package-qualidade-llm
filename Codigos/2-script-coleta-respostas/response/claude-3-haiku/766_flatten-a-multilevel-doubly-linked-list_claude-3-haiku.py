class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None

        curr = head
        while curr:
            if curr.child:
                tail = curr.child
                while tail.next:
                    tail = tail.next
                tail.next = curr.next
                curr.next = curr.child
                curr.child = None
            curr = curr.next
        return head