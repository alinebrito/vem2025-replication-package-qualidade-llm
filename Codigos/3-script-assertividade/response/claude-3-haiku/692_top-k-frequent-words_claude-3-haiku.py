class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = {}
        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
        
        sorted_words = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
        
        return [word for word, _ in sorted_words[:k]]