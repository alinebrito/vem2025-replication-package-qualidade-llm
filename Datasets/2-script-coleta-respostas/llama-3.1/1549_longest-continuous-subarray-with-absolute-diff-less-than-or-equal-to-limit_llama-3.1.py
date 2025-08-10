class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        max_deque, min_deque = [], []
        left = 0
        result = 0

        for right, num in enumerate(nums):
            while max_deque and max_deque[-1] < num:
                max_deque.pop()
            max_deque.append(num)

            while min_deque and min_deque[-1] > num:
                min_deque.pop()
            min_deque.append(num)

            while max_deque and min_deque and max_deque[0] - min_deque[0] > limit:
                if max_deque[0] == nums[left]:
                    max_deque.pop(0)
                if min_deque[0] == nums[left]:
                    min_deque.pop(0)
                left += 1

            result = max(result, right - left + 1)

        return result