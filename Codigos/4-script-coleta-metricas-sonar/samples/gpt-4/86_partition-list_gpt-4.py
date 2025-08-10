class Solution:
    def partition(self, head, x):
        less_head = less_tail = ListNode(0)
        greater_head = greater_tail = ListNode(0)
        
        while head:
            if head.val < x:
                less_tail.next = head
                less_tail = less_tail.next
            else:
                greater_tail.next = head
                greater_tail = greater_tail.next
            head = head.next
        
        greater_tail.next = None
        less_tail.next = greater_head.next
        
        return less_head.next