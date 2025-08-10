class Solution:
  def isPalindrome(self, head):
    fast = slow = head
    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
    
    prev = None
    while slow:
      curr = slow
      slow = slow.next
      curr.next = prev
      prev = curr
    
    left, right = head, prev
    while left and right:
      if left.val != right.val:
        return False
      left = left.next
      right = right.next
    
    # Reverse the second half back to original state
    prev = None
    while curr:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
    
    return True
```

This code utilizes two pointers:

- `fast`: Moves twice as fast as `slow`, reaching the end (or second to last node) when `slow` reaches the middle.
- `slow`: Moves one node at a time, reaching the middle node.
