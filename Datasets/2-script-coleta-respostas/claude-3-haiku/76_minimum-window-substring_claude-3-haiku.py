class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        
        left, right, count, start, min_len = 0, 0, len(t), 0, float("inf")
        
        while right < len(s):
            t_count[s[right]] = t_count.get(s[right], 0) - 1
            if t_count[s[right]] >= 0:
                count -= 1
            
            while count == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left
                
                t_count[s[left]] = t_count.get(s[left], 0) + 1
                if t_count[s[left]] > 0:
                    count += 1
                left += 1
            
            right += 1
        
        return s[start:start+min_len] if min_len != float("inf") else ""