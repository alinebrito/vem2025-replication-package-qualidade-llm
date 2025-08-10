class Solution:
    def maxEnvelopes(self, E: List[List[int]]) -> int:
        E.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, height in E:
            left = 0
            right = len(dp) - 1
            while left <= right:
                mid = (left + right) // 2
                if dp[mid] < height:
                    left = mid + 1
                else:
                    right = mid - 1
            if left == len(dp):
                dp.append(height)
            else:
                dp[left] = height
        return len(dp)
