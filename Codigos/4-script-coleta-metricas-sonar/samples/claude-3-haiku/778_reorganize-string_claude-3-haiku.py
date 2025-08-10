class Solution:
    def reorganizeString(s):
        if not s:
            return ""
        
        from collections import Counter
        count = Counter(s)
        max_count = max(count.values())
        if max_count > (len(s) + 1) // 2:
            return ""
        
        result = []
        for char, freq in count.most_common():
            result.extend([char] * freq)
        
        new_s = ""
        for i in range(0, len(result), 2):
            new_s += result[i]
        for i in range(1, len(result), 2):
            new_s += result[i]
        
        return new_s