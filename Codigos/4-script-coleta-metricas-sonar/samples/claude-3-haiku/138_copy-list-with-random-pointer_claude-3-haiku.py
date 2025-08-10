class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        
        # Create a hash map to store the original nodes and their copies
        node_map = {}
        
        # Iterate through the original linked list and create copies of each node
        curr = head
        while curr:
            new_node = Node(curr.val)
            node_map[curr] = new_node
            curr = curr.next
        
        # Iterate through the original linked list again and set the next and random pointers of the copies
        curr = head
        while curr:
            if curr.next:
                node_map[curr].next = node_map[curr.next]
            if curr.random:
                node_map[curr].random = node_map[curr.random]
            curr = curr.next
        
        return node_map[head]