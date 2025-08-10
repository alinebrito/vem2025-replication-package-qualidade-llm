class Solution:
    class ListNode:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
 self.head = None

    def get(self, index: int) -> int:
        node = self.head
        for _ in range(index):
            if node is None:
                return -1
            node = node.next
        return node.val if node is not None else -1

    def addAtHead(self, val: int) -> None:
 new_node = self.ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = self.ListNode(val)
        else:
            node = self.head
 while node.next:
                node = node.next
            node.next = self.ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            node = self.head
            for _ in range(index - 1):
                if node is None:
                    return                node = node.next
            if node is not None:
                new_node = self.ListNode(val)
                new_node.next = node.next
                node.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
        else:
            node = self.head
            for _ in range(index - 1):
                if node is None:
                    return
                node = node.next
            if node is not None and node.next is not None:
                node.next = node.next.next