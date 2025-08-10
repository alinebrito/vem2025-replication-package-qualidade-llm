class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        concatenated_words = []

        def can_form(word, count):
            if word in word_set and count > 0:
                return True  
            for i in range(1, len(word)):
                prefix, suffix = word[:i], word[i:]
                if prefix in word_set and can_form(suffix, count + 1):
                    return True  
            return False

        for word in words:
            if can_form(word, 0):
                concatenated_words.append(word)

        return concatenated_words  