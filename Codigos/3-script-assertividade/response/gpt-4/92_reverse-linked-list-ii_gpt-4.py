class Solution:
    def reverseBetween(self, head, left, right):
        if left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for _ in range(left - 1):
            prev = prev.next
        
        reverse_start = prev.next
        curr = reverse_start.next
        
        for _ in range(right - left):
            reverse_start.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = reverse_start.next
        
        return dummy.next