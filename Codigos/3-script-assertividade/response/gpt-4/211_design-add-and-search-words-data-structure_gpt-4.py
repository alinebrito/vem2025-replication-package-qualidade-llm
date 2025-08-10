class Solution:
    def __init__(self):
        self.words = set()

    def addWord(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        def match(word1, word2):
            if len(word1) != len(word2):
                return False
            for w1, w2 in zip(word1, word2):
                if w2 != '.' and w1 != w2:
                    return False
            return True

        for w in self.words:
            if match(w, word):
                return True
        return False