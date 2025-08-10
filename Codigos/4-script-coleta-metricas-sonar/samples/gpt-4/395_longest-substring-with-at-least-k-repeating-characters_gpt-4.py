class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0 or k > len(s):
            return 0
        
        max_len = 0  
        unique_chars = len(set(s))
        
        for current_unique in range(1, unique_chars + 1):
            count = {}
            left = 0  
            total_chars = 0  
            valid_chars = 0
            
            for right in range(len(s)):
                if s[right] not in count:
                    count[s[right]] = 0  
                count[s[right]] += 1
                
                if count[s[right]] == k:
                    valid_chars += 1
                
                while len(count) > current_unique:
                    count[s[left]] -= 1  
                    if count[s[left]] == k - 1:
                        valid_chars -= 1  
                    if count[s[left]] == 0:
                        del count[s[left]]
                    left += 1
                
                if valid_chars == len(count):
                    max_len = max(max_len, right - left + 1)
        
        return max_len  