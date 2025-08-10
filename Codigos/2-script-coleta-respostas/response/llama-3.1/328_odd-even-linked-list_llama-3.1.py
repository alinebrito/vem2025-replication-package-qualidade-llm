class Solution:
    def oddEvenList(self, head):
        if not head:
            return head
        odd = head
        even = head.next
        even_head = even
        while not even or not even.next:
            if not even:
                break
            odd.next = even.next
            odd = odd.next
            if not odd:
                break
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head