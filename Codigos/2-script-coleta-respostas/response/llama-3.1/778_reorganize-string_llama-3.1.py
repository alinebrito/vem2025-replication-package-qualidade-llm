class Solution:
    def reorganizeString(self, S):
        from collections import Counter
        count = Counter(S)
        max_count = max(count.values())
        if max_count > (len(S) + 1) // 2:
            return ""
        result = []
        for char, freq in count.most_common():
            result.extend([char] * freq)
        res = []
        for i in range(len(result)):
            if i % 2 == 0:
                res.append(result[i // 2])
            else:
                res.append(result[len(result) - 1 - i // 2])
        return ''.join(res)