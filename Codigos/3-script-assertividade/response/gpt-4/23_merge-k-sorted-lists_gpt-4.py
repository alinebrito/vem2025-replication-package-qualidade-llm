class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return []
        import heapq
        min_heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l[0], i, 0))
        result = []
        while min_heap:
            val, list_idx, element_idx = heapq.heappop(min_heap)
            result.append(val)
            if element_idx + 1 < len(lists[list_idx]):
                heapq.heappush(min_heap, (lists[list_idx][element_idx + 1], list_idx, element_idx + 1))
        return result