class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        from heapq import heappush, heappop
        heap = []
        for i, lst in enumerate(lists):
            if lst:
                heappush(heap, (lst.val, i, lst))

        dummy = ListNode(0)
        curr = dummy
        while heap:
            _, i, node = heappop(heap)
            curr.next = node
            curr = curr.next
            node = node.next
            if node:
                heappush(heap, (node.val, i, node))

        return dummy.next