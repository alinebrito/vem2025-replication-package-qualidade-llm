class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        from typing import List
        from heapq import heappush, heappop

        def get_median(min_heap, max_heap):
            if len(min_heap) == len(max_heap):
                return (-max_heap[0] + min_heap[0]) / 2
            else:
                return -max_heap[0]

        min_heap, max_heap = [], []
        result = []

        for i in range(len(nums)):
            if len(min_heap) < len(max_heap):
                heappush(min_heap, -heappushpop(max_heap, -nums[i]))
            else:
                heappush(max_heap, -heappushpop(min_heap, nums[i]))

            if i >= k - 1:
                result.append(get_median(min_heap, max_heap))

                if nums[i - k + 1] <= -max_heap[0]:
                    heappop(max_heap)
                else:
                    heappop(min_heap)

        return result