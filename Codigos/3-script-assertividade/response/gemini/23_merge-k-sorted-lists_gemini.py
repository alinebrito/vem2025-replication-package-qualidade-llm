class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        # Use a min-heap to store the nodes from different lists
        import heapq
        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, head))

        # Merge the nodes from the heap into a new linked list
        dummy = ListNode()
        curr = dummy
        while heap:
            val, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))

        return dummy.next