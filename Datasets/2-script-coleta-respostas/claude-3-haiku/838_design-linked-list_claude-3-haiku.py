class Solution:
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = self.head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            new_node = ListNode(val)
            new_node.next = current.next
            current.next = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            if index == self.size - 1:
                self.tail = current
            current.next = current.next.next
        self.size -= 1

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next