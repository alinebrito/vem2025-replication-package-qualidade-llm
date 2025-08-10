class Solution:
    def copyRandomList1(self, head):
        if not head:
            return None
        
        old_to_new = {}
        current = head
        
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next
        
        current = head
        
        while current:
            new_node = old_to_new[current]
            new_node.next = old_to_new.get(current.next)
            new_node.random = old_to_new.get(current.random)
            current = current.next
        
        return old_to_new[head]