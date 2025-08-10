class Solution:
    def reverseBetween(self, head, left, right):
        if left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        prev, curr = dummy, head
        for _ in range(left - 1):
            prev, curr = curr, curr.next
        
        tail = curr
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        return dummy.next