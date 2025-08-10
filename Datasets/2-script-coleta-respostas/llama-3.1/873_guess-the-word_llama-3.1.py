class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        for _ in range(10):
            guess = self.most_common_word(wordlist)
            result = master.guess(guess)
            if result == 6:
                return
            wordlist = [word for word in wordlist if self.match_count(guess, word) == result]

    def most_common_word(self, wordlist: List[str]) -> str:
        max_count = 0
        max_word = ""
        for word in wordlist:
            count = sum([sum(c1 == c2 for c1, c2 in zip(word, w)) for w in wordlist])
            if count > max_count:
                max_count = count
                max_word = word
        return max_word

    def match_count(self, word1: str, word2: str) -> int:
        return sum(c1 == c2 for c1, c2 in zip(word1, word2))