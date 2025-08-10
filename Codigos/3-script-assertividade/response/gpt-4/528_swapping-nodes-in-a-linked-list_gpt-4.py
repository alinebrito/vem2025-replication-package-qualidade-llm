class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        first = last = head  
        count = 1  
        while count < k:
            first = first.next  
            count += 1  
        temp = first  
        while temp.next:
            last = last.next  
            temp = temp.next  
        first.val, last.val = last.val, first.val  
        return head  