class Solution:
    def pairSum(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        maxSum = 0
        while prev:
            maxSum = max(maxSum, head.val + prev.val)
            head = head.next
            prev = prev.next
        return maxSum