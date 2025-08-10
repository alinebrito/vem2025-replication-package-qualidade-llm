class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = deque()
        result = []
        for i, num in enumerate(nums):
            while deque and nums[deque[-1]] < num:
                deque.pop()
            deque.append(i)
            if deque[0] == i - k:
                deque.popleft()
            if i >= k - 1:
                result.append(nums[deque[0]])
        return result