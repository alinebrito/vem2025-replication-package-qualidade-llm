class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getNumber(node):
            num = 0
            while node:
                num = num * 10 + node.val
                node = node.next
            return num
        
        sum_value = getNumber(l1) + getNumber(l2)
        dummy = ListNode(0)
        current = dummy
        
        for digit in str(sum_value):
            current.next = ListNode(int(digit))
            current = current.next
        
        return dummy.next