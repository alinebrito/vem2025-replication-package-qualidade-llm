class Solution:
    def reorganizeString(self, S):
        from collections import Counter  
        count = Counter(S)
        max_count = max(count.values())
        if max_count > (len(S) + 1) // 2:
            return ""
        result = []
        max_heap = sorted(count.items(), key=lambda x: -x[1])
        while len(max_heap) > 1:
            first = max_heap.pop(0)
            second = max_heap.pop(0)
            result.append(first[0])
            result.append(second[0])
            if first[1] > 1:
                max_heap.append((first[0], first[1] - 1))
            if second[1] > 1:
                max_heap.append((second[0], second[1] - 1))
            max_heap.sort(key=lambda x: -x[1])
        if max_heap:
            result.append(max_heap[0][0])
        return ''.join(result)