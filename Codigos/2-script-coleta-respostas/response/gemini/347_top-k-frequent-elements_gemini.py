class Solution:
    def topKFrequent(self, nums, k):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []
        for num, count in freq.items():
            heappush(heap, (-count, num))
            if len(heap) > k:
                heappop(heap)

        return [num for _, num in heap]