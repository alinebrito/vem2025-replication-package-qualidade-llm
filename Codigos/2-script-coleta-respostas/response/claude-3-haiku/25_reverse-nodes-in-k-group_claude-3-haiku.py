class Solution:
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        
        while r:
            for _ in range(k):
                if not r: return dummy.next
                r = r.next
            
            nex = self.reverseList(l, r)
            l.next = nex
            jump.next = l
            jump = l
            l = r
        
        return dummy.next
    
    def reverseList(self, head, tail):
        prev = tail
        while head != tail:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev