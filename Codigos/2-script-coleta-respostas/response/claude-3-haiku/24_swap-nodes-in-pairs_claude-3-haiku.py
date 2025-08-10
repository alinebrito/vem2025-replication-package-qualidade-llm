class Solution:
    def swapPairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return self.next