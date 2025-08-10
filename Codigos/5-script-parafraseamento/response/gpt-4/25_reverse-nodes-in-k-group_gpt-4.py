class Solution:
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = head  
        count = 0
        
        while head:
            count += 1  
            head = head.next
            
        while count >= k:
            cur = jump.next  
            prev = None  
            for _ in range(k):
                tmp = cur.next  
                cur.next = prev  
                prev = cur  
                cur = tmp  
            tail = jump.next  
            jump.next = prev  
            tail.next = cur  
            jump = tail  
            count -= k
            
        return dummy.next  