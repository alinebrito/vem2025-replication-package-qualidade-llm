class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        result = []
        for word in words:
            if self.can_be_formed(word, word_set, {}):
                result.append(word)
        return result

    def can_be_formed(self, word, word_set, memo):
        if word in memo:
            return memo[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in word_set and (suffix in word_set or self.can_be_formed(suffix, word_set, memo)):
                memo[word] = True
                return True
        memo[word] = False