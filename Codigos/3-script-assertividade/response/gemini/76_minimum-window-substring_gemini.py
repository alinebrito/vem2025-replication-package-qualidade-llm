class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, have = {}, {}
        for char in t:
            need[char] = need.get(char, 0) + 1
        
        start = 0
        end = 0
        min_len = float('inf')
        count = 0
        
        while end < len(s):
            char = s[end]
            have[char] = have.get(char, 0) + 1
            
            if char in need and have[char] <= need[char]:
                count += 1
            
            while start <= end and count == len(need):
                char = s[start]
                if min_len > end - start + 1:
                    min_len = end - start + 1
                    min_start = start
                
                have[char] -= 1
                if char in need and have[char] < need[char]:
                    count -= 1
                start += 1
            
            end += 1
        
        return s[min_start:min_start + min_len] if min_len != float('inf') else ""