class Solution:
 def swapPairs(self, head):
        pre = self
        pre.next = head
        while pre.next and pre.next.next:
            first = pre.next
            second = pre.next.next
            pre.next = second
            first.next = second.next
            second.next = first
            pre = first
        return self.next