class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        k %= length
        if k == 0:
            return head
        tail.next = head
        steps = length - k
        newTail = head
        while steps > 1:
            newTail = newTail.next
            steps -= 1
        newHead = newTail.next
        newTail.next = None
        return newHead