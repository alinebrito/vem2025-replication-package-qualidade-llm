class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        while curr:
            next_ptr = curr.next
            while dummy.next != curr:
                if dummy.next.val > curr.val:
                    temp = dummy.next
                    dummy.next = curr
                    curr.next = temp
                    break
                else:
                    dummy = dummy.next
            curr = next_ptr
            dummy = head
        return head