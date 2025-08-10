class Solution:
    def topKFrequent(self, words, k):
        freq_map = {}
        for word in words:
            freq_map[word] = freq_map.get(word, 0) + 1
        sorted_words = sorted(freq_map.keys(), key=lambda x: (-freq_map[x], x))
        return sorted_words[:k]