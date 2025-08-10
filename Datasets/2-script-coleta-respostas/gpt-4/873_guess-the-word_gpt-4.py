class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def match_count(word1, word2):
            return sum(c1 == c2 for c1, c2 in zip(word1, word2))

        for _ in range(10):
            guess = words[0]
            count = master.guess(guess)
            if count == 6:
                return
            words = [word for word in words if match_count(guess, word) == count]