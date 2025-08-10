class Solution:
    def getDecimalValue(self, head):
        decimal_value = 0
        while head:
            decimal_value = decimal_value * 2 + head.val
            head = head.next
        return decimal_value