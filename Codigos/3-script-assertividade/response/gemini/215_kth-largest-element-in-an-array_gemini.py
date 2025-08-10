class Solution:
    def findKthLargest(self, nums, k):
        # Create a min-heap to store the k largest elements
        heap = []

        # Insert the first k elements into the heap
        for num in nums[:k]:
            heapq.heappush(heap, num)

        # Process the remaining elements
        for num in nums[k:]:
            # If the current element is larger than the smallest element in the heap,
            # replace the smallest element with the current element
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        # The kth largest element is the smallest element in the heap
        return heap[0]