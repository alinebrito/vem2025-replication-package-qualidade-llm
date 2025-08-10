class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = {}
        for word in words:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

        sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        return [word for word, freq in sorted_count[:k]]