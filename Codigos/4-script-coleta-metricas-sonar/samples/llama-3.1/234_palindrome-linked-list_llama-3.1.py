class Solution:
    def isPalindrome(self, head):
        rev = None

        while head:
            temp = head.next
            head.next = rev
            rev = head
            head = temp

        while rev:
            if rev.val!= temp.val:
                return False
            rev = rev.next
            temp = temp.next
        return True