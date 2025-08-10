class Solution:
    def mergeKLists(self, lists):
        class ListNode:
            def __init__(self, x):
                self.val = x                self.next = None

        dummy = ListNode(0)
        current = dummy        while True:
            min_val = float('inf')
            min_list = None
            for i, lst in enumerate(lists):
                if lst and lst.val < min_val:
                    min_val = lst.val
                    min_list = i

            if min_list is None:
                break

            current.next = lists[min_list]
            current = current.next
            lists[min_list] = lists[min_list].next

        result = []
        current = dummy.next
 while current:
            result.append(current.val)
            current = current.next

        return result