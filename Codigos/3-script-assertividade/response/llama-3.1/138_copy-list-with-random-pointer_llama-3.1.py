class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        old_node_map = {}
        cur = head
        while cur:
            new_node = Node(cur.val)
            old_node_map[cur] = new_node
            cur = cur.next

        cur = head
        new_head = old_node_map[head]
        new_cur = new_head
        while cur:
            new_cur.next = old_node_map.get(cur.next)
            new_cur.random = old_node_map.get(cur.random)
            cur = cur.next
            new_cur = new_cur.next
        return new_head

class Node:
    def __init__(self, x: int):
        self.val = x
        self.next = None
        self.random = None
