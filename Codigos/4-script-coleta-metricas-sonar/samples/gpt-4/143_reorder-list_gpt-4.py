class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None
        
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2