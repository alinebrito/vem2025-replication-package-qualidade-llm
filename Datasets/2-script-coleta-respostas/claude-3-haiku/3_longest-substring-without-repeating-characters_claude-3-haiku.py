class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_length = 0
        start = 0
        
        for i, char in enumerate(s):
            if char in seen and seen[char] >= start:
                start = seen[char] + 1
            else:
                max_length = max(max_length, i - start + 1)
            seen[char] = i
        
        return max_length