class Solution:
    def copyRandomList1(self, head):
        if not head:
            return None
        curr = head
        while curr:
            next_node = curr.next
            copy = Node(curr.val)
            curr.next = copy
            copy.next = next_node
            curr = next_node
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        curr = head
        copy_head = head.next
        copy_curr = copy_head
        while curr:
            curr.next = curr.next.next
            curr = curr.next
            if copy_curr.next:
                copy_curr.next = copy_curr.next.next
                copy_curr = copy_curr.next
        return copy_head