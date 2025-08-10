class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        result = []
        for i in range(n - k + 1):
            window = sorted(nums[i: i + k])
            if k % 2 == 0:
                median = (window[k // 2 - 1] + window[k // 2]) / 2
            else:
                median = window[k // 2]
            result.append(median)
        return result