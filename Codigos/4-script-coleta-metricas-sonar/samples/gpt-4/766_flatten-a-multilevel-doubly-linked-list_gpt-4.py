class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return None
        
        stack = []
        curr = head  
        prev = None
        
        while curr or stack:
            if curr:
                if prev:
                    prev.next = curr  
                    curr.prev = prev  
                stack.append(curr)
                prev = curr  
                curr.child = None  
                curr = curr.child if curr.child else curr.next  
            else:
                curr = stack.pop()
                curr = curr.next
        
        return head  