class Solution:
    def detectCycle(self, head):
        slow = fast = head  
        while fast and fast.next:
            slow = slow.next  
            fast = fast.next.next  
            if slow == fast:
                entry = head  
                while entry != slow:
                    entry = entry.next  
                    slow = slow.next  
                return entry  
        return None  