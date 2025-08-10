class Solution:
    def topKFrequent(self, words, k):
        from collections import Counter
        count = Counter(words)
        return sorted(count, key=lambda word: (-count[word], word))[:k]