class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        result = []

        def dfs(word):
            if not word:
                return True
            for i in range(1, len(word) + 1):
                if word[:i] in word_set and dfs(word[i:]):
                    return True
            return False

        for word in words:
            if dfs(word):
                result.append(word)

        return result