class Solution:
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow.next, rev, slow = rev, slow, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        return not rev