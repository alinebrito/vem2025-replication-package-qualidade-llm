class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = defaultdict(int)
        for char in t:
            t_count[char] += 1

        required = len(t_count)
        formed = 0
        window_counts = {}
        min_length = float('inf')
        left, right = 0, 0
        ans = ""

        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1

            while formed == required and left <= right:
                char = s[left]

                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    ans = s[left:right + 1]

                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1

                left += 1

            right += 1

        return ans