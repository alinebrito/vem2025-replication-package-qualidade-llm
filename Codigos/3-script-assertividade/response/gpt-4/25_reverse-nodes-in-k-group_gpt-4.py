class Solution:
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = head
        count = 0
        
        while head:
            count += 1
            head = head.next
        
        while count >= k:
            curr = dummy.next
            nex = curr.next
            for _ in range(1, k):
                curr.next = nex.next
                nex.next = dummy.next
                dummy.next = nex
                nex = curr.next
            dummy = curr
            count -= k
        
        return dummy.next